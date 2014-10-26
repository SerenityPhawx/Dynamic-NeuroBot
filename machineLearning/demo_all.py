#!/usr/bin/env python

from readData2 import *
from readData2 import *
from timeFreq import *

import scipy
import numpy as np
import pylab
import sklearn
from sklearn import svm
import pickle
from sklearn.externals import joblib

INPUT_FILE = "berger.csv"

sensor1ID = 3
sensor2ID = 4
X1, X2 = readInput(INPUT_FILE, sensor1ID, sensor2ID)

def getPredictions(X1, X2):
   fourier1 = timeFreq(X1[:,2])
   fourier2 = timeFreq(X2[:,2])
   isTrial = reshapeIsTrialLabels(X1[:,3])
   trials = np.where(isTrial)[0]
   labels = reshapeStateLabels(X1[:,4])[trials]

   #X = sklearn.preprocessing.normalize(np.column_stack((fourier1[trials], fourier2[trials])))
   X = sklearn.preprocessing.normalize(np.column_stack((fourier1[trials], fourier2[trials])))

   svc = joblib.load('bergerSVMclassifier.pkl')
   return(svc.predict(X))

def doAttractor(data):
	#Find Tau (time delay variable)
	tau_max = 100
	minf = []     #mutual information between delayed and nondelayed series

	#Measure mutual info up to a max value

	for tau in range(1, tau_max):
		non_delayed = data[:-tau]
		delayed = np.roll(data, -tau)[:-tau]   #roll funct performs delay by shifting all values to the left by tau
		joint = np.hstack((non_delayed, delayed))   #series must be shortened by tau values, if data series is a fixed length with no further values to shift in
		minf.append(sklearn.metrics.normalized_mutual_info_score(non_delayed, delayed))
		
	#Return 1st local min of mutual info
		if len(minf) > 1 and minf[-2] < minf[-1]:   #if current mutual info value > previous one
			tau -= 100
			print(tau, minf)
			break
	return data


dataattr = doAttractor(X1)
datasvm  = getPredictions(X1, X2)

#Plot time-delayed embedding in 3 Dimensions using tau

figure = pylab.figure()
axes = Axes3D(figure)
data_lag0 = dataattr[:-2].flatten()
data_lag1 = np.roll(dataattr, -tau)[:-2].flatten()
data_lag2 = np.roll(dataattr, -2*tau)[:-2].flatten()

axes.plot3D(data_lag0, data_lag1, data_lag2)
figure.add_axes(axes)

pylab.show()

