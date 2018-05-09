import numpy as np
import os
import inspect
from sklearn.neural_network import MLPClassifier
from sklearn import datasets

workingDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# npzfile = np.load(os.path.join(workingDir, "t5dataset1.npz"))

# 100 X 1 matrix
# x = npzfile['x']
# corresponding 100 x 1 matrix
# y = npzfile['y']

digits = datasets.load_digits()
x = digits.data
y = digits.target

# create a MLP regressor model
# choice of 'relu', 'tanh', 'identity' (linear) and 'logistic' (sigmoid)
clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(10, 6), activation='relu', max_iter=500)

# train the network
clf.fit(x, y)
# to get weights and biases call clf.get_params()

score = clf.score(x, y)
# perfect score is 1.0

# computer the network output
yhat = clf.predict(x)

# compute the MSE
mse = np.mean(np.square(y - yhat))

print("Score: ")
print(score)
print("1 - MSE: ")
print(1-mse)

