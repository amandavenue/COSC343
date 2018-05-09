import numpy as np
import os
import inspect
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

workingDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

npzfile = np.load(os.path.join(workingDir, "t5dataset1.npz"))

# 100 X 1 matrix
x = npzfile['x']
# corresponding 100 x 1 matrix
y = npzfile['y']

# create a MLP regressor model
# choice of 'relu', 'tanh', 'identity' (linear) and 'logistic' (sigmoid)
clf = MLPRegressor(alpha=1e-5, hidden_layer_sizes=(32, 9), activation='relu', max_iter=500)

# train the network
clf.fit(x, y)
# to get weights and biases call clf.get_params()

score = clf.score(x, y)
# perfect score is 1.0

# computer the network output
yhat = clf.predict(x)

# compute the MSE
mse = np.mean(np.square(y - yhat))

plt.close('all')
plt.figure()

plt.plot(x, y, 'b.')
plt.plot(x, yhat, 'r-')

print("Score: ", score)
print("1 - MSE: ", 1-mse)

plt.legend(['sample data', 'my function'])
plt.xlabel('x')
plt.ylabel('y')

plt.show()
