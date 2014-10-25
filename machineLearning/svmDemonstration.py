# A quick demonstration how to use an SVM classifier with scikit-learn 

from sklearn import svm
import numpy as np

N = 1000
mean1 = np.array([2,2])

train = np.random.multivariate_normal(mean=[0,0], cov=np.eye(2), size=N)  # Generate random data
trainLabels = np.random.binomial(n=1,p=0.5,size=N)
train = train + np.array([mean1 * i for i in trainLabels]) # Translate randomly chosen examples by mean1


## Do the same to create some test data
test = np.random.multivariate_normal(mean=[0,0], cov=np.eye(2), size=N)
testLabels = np.random.binomial(n=1,p=0.5,size=N)
test = test + np.array([mean1 * i for i in testLabels])


svmClassifier = svm.SVC()
svmClassifier.fit(train, trainLabels)  # Train SVM classifier

predictions = svmClassifier.predict(test) # Predict labels of test data
np.sum(np.abs(predictions - testLabels)) / np.float(N) # Calculate accuracy