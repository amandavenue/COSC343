import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn import datasets
import matplotlib.pyplot as plt

# 100 X 1 matrix
# x = npzfile['x']
# corresponding 100 x 1 matrix
# y = npzfile['y']

diabetes = datasets.load_diabetes()
x = diabetes.data
y = diabetes.target

def split_data(x, y):
    num_points, num_attributes = x.shape
    I = np.random.permutation(num_points)
    # x = x[i, :]
    # y = y[i, :]
    split = int(np.floor(num_points * 0.8))
    Itrain = I[0:split]

    xtrain = x[Itrain, :]
    ytrain = y[Itrain,]

    Itest = I[split:-1]
    xtest = x[Itest, :]
    ytest = y[Itest,]

    return xtrain, ytrain, xtest, ytest

xtrain, ytrain, xtest, ytest = split_data(x, y)

# create a MLP regressor model
# choice of 'relu', 'tanh', 'identity' (linear) and 'logistic' (sigmoid)
clf = MLPRegressor(alpha=1e-5, hidden_layer_sizes=(200, 100), activation='relu', max_iter=5000)

# train the network
clf.fit(xtrain, ytrain)
# to get weights and biases call clf.get_params()

trainscore = clf.score(xtrain, ytrain)
# computer the network output
trainyhat = clf.predict(xtrain)
# compute the MSE
trainmse = np.mean(np.square(ytrain - trainyhat))

testscore = clf.score(xtest, ytest)
# computer the network output
testyhat = clf.predict(xtest)
# compute the MSE
testmse = np.mean(np.square(ytest - testyhat))


print("Trained MSE: ")
print(trainmse)
print("Test MSE: ")
print(testmse)

plt.close('all')
plt.figure()

plt.plot(x, y, 'b.')
plt.plot(xtrain, trainyhat, 'r-')

plt.legend(['sample data', 'my function'])
plt.xlabel('x')
plt.ylabel('y')

plt.show()