import numpy as np
   
def readInput(filename, sensor1ID = 1, sensor2ID = 2):
   XInput = np.recfromcsv(INPUT_FILE)
   
   X1 = X[:, np.where(XInput[:,0] == sensor1ID)[0]]
   X2 = X[:, np.where(XInput[:,0] == sensor2ID)[0]]
   N = np.min(X1.shape[0], X2.shape[0])
   
   X1 = X1[:N-1,:]
   X2 = X2[:N-1,:]
   
   return(X1, X2)