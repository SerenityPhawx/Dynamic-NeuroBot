#!/usr/bin/env python
from readData import *
from timeFreq import *
import scipy
import numpy as np
import sklearn
from sklearn import svm

INPUT_FILE = "raw_dat.01_26_05.csv"
sensor1ID = 4


#filename = INPUT_FILE
#X1, X2 = readInput(filename, sensor1ID)

WINDOW_LENGTH=500
LIMIT = 500
SAMPLING_RATE=500
d = 1/SAMPLING_RATE

n= 100000
N = 2 * n
alphaFreq = 12
otherFreqs = [3,8,20]
noiseSigma = 0.5
alpha2Weight = 3

alpha1 = np.sin(alphaFreq * (n / SAMPLING_RATE) * np.linspace(0, 2 * np.pi, n))
alpha2 = alpha2Weight * np.sin(alphaFreq * (n / SAMPLING_RATE) * np.linspace(0, 2 * np.pi, n))
alpha = np.concatenate((alpha1, alpha2))

otherSignal = np.sum(np.column_stack([np.sin(freq * (N / SAMPLING_RATE) * np.linspace(0, 2 * np.pi, N)) for freq in otherFreqs]), axis=1)
noise = np.random.normal(0,noiseSigma,N)
signal = alpha + otherSignal + noise



#X11 = np.sin(np.linspace(1, 10000, 10000)) + np.random.normal(0,0.5,size=10000)
#X12 = np.sin(2 * np.linspace(1, 10000, 10000)) + np.random.normal(0,0.5,size=10000)
#X1 = np.repeat((X11, X12),10)
#X2 = X1
labels = np.concatenate((np.zeros(n), np.ones(n)))

X1 = np.column_stack((np.zeros((N,2)), signal, np.ones((N,1)), labels))
#X2 = np.column_stack((np.zeros((N,2)), X2, np.ones((10,1)), labels))

fourier1 = timeFreq(X1[:,2])
#fourier2 = timeFreq(X2[:,2])
isTrial = reshapeIsTrialLabels(X1[:,3])
trials = np.where(isTrial)[0]
labels = reshapeStateLabels(X1[:,4])


   #X = sklearn.preprocessing.normalize(np.column_stack((fourier1[trials], fourier2[trials])))
X = sklearn.preprocessing.normalize(fourier1[trials])
labels = labels[trials]

   # Randomly permute samples
perm = np.random.permutation(X.shape[0])
X = X[perm]
labels = labels[perm]

nTrain = int(X.shape[0] / 2)
trainX = X[:nTrain]
trainLabels = labels[:nTrain]

testX = X[nTrain+1:]
testLabels = labels[nTrain+1:]

svc = svm.SVC()
svc.fit(trainX, trainLabels)
