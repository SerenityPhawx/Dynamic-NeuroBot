# Use this file if working with 2 Sensor
#!/usr/bin/env python
from readData2 import *
from timeFreq import *
import scipy
import numpy as np
import sklearn
from sklearn import svm
import pickle
from sklearn.externals import joblib

INPUT_FILE = "berger.csv"
sensor1ID = 3
sensor2ID = 4


filename = INPUT_FILE
X1, X2 = readInput(filename, sensor1ID, sensor2ID)
#N= 10000
#X11 = np.sin(np.linspace(1, 10000, 10000)) + np.random.normal(0,0.5,size=10000)
#X12 = np.sin(2 * np.linspace(1, 10000, 10000)) + np.random.normal(0,0.5,size=10000)
#X1 = np.repeat((X11, X12),10)
#X2 = X1
#labels = np.repeat((np.ones(N), np.zeros(N)),10)

#X1 = np.column_stack((np.zeros((2*N*10,2)), X1, np.ones((2*N*10,1)), labels))
#X2 = np.column_stack((np.zeros((2*N*10,2)), X2, np.ones((2*N*10,1)), labels))

fourier1 = timeFreq(X1[:,2])
fourier2 = timeFreq(X2[:,2])
isTrial = reshapeIsTrialLabels(X1[:,3])
trials = np.where(isTrial)[0]
labels = reshapeStateLabels(X1[:,4])


   #X = sklearn.preprocessing.normalize(np.column_stack((fourier1[trials], fourier2[trials])))
X = sklearn.preprocessing.normalize(np.column_stack((fourier1[trials], fourier2[trials])))
labels = labels[trials]

   # Randomly permute samples
perm = np.random.permutation(X.shape[0])
X = X[perm]
labels = labels[perm]

nTrain = int(X.shape[0] * 9/10.)
trainX = X[:nTrain]
trainLabels = labels[:nTrain]

testX = X[nTrain+1:]
testLabels = labels[nTrain+1:]

# Chosen the following params using tryParams (but we don't have enough data to do cross validation / testing properly, so it's probably not sound...)
C = 100 
gamma = 0.1 #
svc = svm.SVC(C=C, gamma=gamma)
svc.fit(trainX, trainLabels)

joblib.dump(svc, 'bergerSVMclassifier.pkl')


def tryParam(C, Gamma):
   svc = svm.SVC(C=C, gamma=Gamma)
   svc.fit(trainX, trainLabels)
   errTrain = np.sum(np.abs(svc.predict(trainX) - trainLabels)) / trainLabels.size
   errTest = np.sum(np.abs(svc.predict(testX) - testLabels)) / testLabels.size
   return((errTrain, errTest))

def tryParams():
   Pens = [1,10,100,500,1000,10000]
   Gammas = [0.01,0.1,1,10,100]
   return([(P, Gamma, tryParam(P, Gamma)) for P in Pens for Gamma in Gammas])

