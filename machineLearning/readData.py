import numpy as np

INPUT_FILE = "data.csv"
   
def readInput(filename = INPUT_FILE, sensor1ID = 1, sensor2ID = 2):
   XInput = np.recfromcsv(INPUT_FILE)
   
   X1 = X[:, np.where(XInput[:,0] == sensor1ID)]
   X2 = X[:, np.where(XInput[:,0] == sensor2ID)]
   N = np.min(X1.shape[0], X2.shape[0])
   
   X1 = X1[:N-1,:]
   X2 = X2[:N-1,:]
   
   return(X1, X2)