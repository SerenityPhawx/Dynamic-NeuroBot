import scipy
import numpy as np

SAMPLING_RATE = 250
WINDOW_LENGTH=64


def fftBins(signal):
   ft = np.fft.rfft(signal * np.hamming(signal.shape[1]))
   return(np.abs(ft))


def timeFreq(signal):
   signal = np.concatenate((signal, np.zeros((-signal.size) % WINDOW_LENGTH))) #padd with zeros to have shapes match up 
   X = np.reshape(signal, newshape=(-1,WINDOW_LENGTH))
   return(fftBins(X))

def reshapeIsTrialLabels(trialLabels):
   trialLabels = np.concatenate((trialLabels, np.zeros((-trialLabels.size) % WINDOW_LENGTH)))
   trialLabels = np.reshape(trialLabels, newshape=(-1,WINDOW_LENGTH))
   return(np.all(trialLabels, axis=1))

def reshapeStateLabels(stateLabels):
   stateLabels = np.concatenate((stateLabels, np.zeros((-stateLabels.size) % WINDOW_LENGTH)))
   stateLabels = np.reshape(stateLabels, newshape=(-1,WINDOW_LENGTH))
   return(np.int32(np.round(np.mean(stateLabels, axis=1))))
   