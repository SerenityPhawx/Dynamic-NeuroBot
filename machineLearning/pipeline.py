#!/usr/bin/env python
from readData import *
from timeFreq import *
import scipy
import numpy as np
from sklearn import svm

INPUT_FILE = "data.csv"

#X1, X2 = readInput(INPUT_FILE)
X1 = np.sin(np.linspace(1, 100, 1000)) + np.random.normal(0,0.2,size=1000)
X2 = np.sin(np.linspace(1, 100, 1000)) + np.random.normal(0,0.2,size=1000)

X1 = np.column_stack((np.zeros((1000,2)), X1, np.ones((1000,2))))
X2 = np.column_stack((np.zeros((1000,2)), X2, np.ones((1000,2))))


fourier1 = timeFreq(X1[:,2])
fourier2 = timeFreq(X2[:,2])
isTrial = reshapeIsTrialLabels(X1[:,3])
trials = np.where(isTrial)[0]
labels = reshapeStateLabels(X1[:,4])


X = np.column_stack((fourier1[trials], fourier2[trials], labels[trials]))