import scipy
import numpy as np

SAMPLING_RATE = 250
WINDOW_LENGTH=64


def fftBins(signal):
   ft = np.fft.rfft(signal * np.hamming(signal.shape[1]))
   return(ft)


def timeFreq(X):
   X = np.concatenate((X, np.zeros((-X.size) % WINDOW_LENGTH))) #padd with zeros to have shapes match up 
   Y = np.reshape(X, newshape=(-1,WINDOW_LENGTH))
   return(fftBins(Y))