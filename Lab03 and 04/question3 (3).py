#!/usr/bin/env python3
from Perceptron import Perceptron
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import preprocessing
import time

plot_handles = []

def get_data():
    digits = datasets.load_digits()
    x = digits.data
    y = digits.target
    y = np.expand_dims(y, axis=1)
    enc = preprocessing.OneHotEncoder()
    enc.fit(y)
    y = enc.transform(y).toarray()

    return x, y


def split_data(x, y):
    num_points, num_attributes = x.shape
    i = np.random.permutation(num_points)
    x = x[i, :]
    y = y[i, :]
    split = int(np.floor(num_points * 0.8))
    xtrain = x[0:split, :]
    ytrain = y[0:split, :]
    xtest = x[split:, :]
    ytest = y[split:, :]

    return xtrain, ytrain, xtest, ytest


def get_yhat_test(x, w, b, n):
    yhat = np.matmul(x[n, :], w.transpose())-b
    for i in range(0, 10):
        if yhat[i] >= 0:
            yhat[i] = 1
        else:
            yhat[i] = 0
    return yhat


def data_plot(x, y=None):
    global plot_handles
    num_points, num_attributes = x.shape
    im_height = 8
    im_width = 8

    if not plot_handles:
        plt.close('all')
        figure_handle = plt.figure()
        plt.ion()
        plt.show()
        n = 0
        for r in range(4):
            for c in range(4):
                if num_points <= n:
                    continue

                im = x[n, :].reshape(im_height, im_width)
                n += 1
                ph = figure_handle.add_subplot(4, 4, n)
                plot_handles.append(ph)
                ph.imshow(im)
                ph.xaxis.set_visible(False)
                ph.yaxis.set_visible(False)

    for n in range(len(plot_handles)):
        if np.sum(y[n, :]) != 1:
            class_label = "?"
        else:
            class_label = np.argmax(y[n, :])

        plot_handles[n].set_title(class_label)

    plt.pause(0.1)
    time.sleep(0.1)


# set x and y to the data from sklearn data
x, y = get_data()
# split up the data into training and testing
xtrain, ytrain, xtest, ytest = split_data(x, y)

number_train_inputs, _ = xtrain.shape
number_test_inputs, _ = xtest.shape

max_epochs = 1000

# make 10 perceptrons, one to deal with each
p0 = Perceptron()
p1 = Perceptron()
p2 = Perceptron()
p3 = Perceptron()
p4 = Perceptron()
p5 = Perceptron()
p6 = Perceptron()
p7 = Perceptron()
p8 = Perceptron()
p9 = Perceptron()

# make a list of the perceptrons (so I can iterate through them)
perceptrons = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]

for i in range(max_epochs):
    # 10 x 64 weight matrix
    weights = np.zeros((10, 64))
    # 1 x 10 bias matrix
    bias = np.zeros(10)

    for index, perceptron in enumerate(perceptrons):

        perceptron.train(xtrain, ytrain[:, index], 0.01)
        weights[index, :] = perceptron.get_weights()
        bias[index] = perceptron.get_bias()

    incorrect_tests = 0
    y_hat = np.zeros(ytest.shape)

    for n in range(number_test_inputs):

        yhat = get_yhat_test(xtest, weights, bias, n)
        found_one = 0
        value = -1
        for m in range(0, 10):
            if yhat[m] == 1:
                if found_one == 0:
                    found_one = 1
                    value = m
                else:
                    found_one = 0
                    break
        # No 1's or too many 1's - doesn't know what number it is
        if found_one == 0:
            incorrect_tests += 1
        # Wrong decision
        elif ytest[n, value] == 0:
            incorrect_tests += 1

        y_hat[n, :] = yhat

    if incorrect_tests == 0:
        print("Successfully labelled.")
        break

    incorrect_trains = 0
    for u in range(number_train_inputs):
        yhat = get_yhat_test(xtrain, weights, bias, u)
        found_one = 0
        value = -1
        for v in range(0, 10):
            if yhat[v] == 1:
                if found_one == 0:
                    found_one = 1
                    value = v
                else:
                    found_one = 0
                    break
        # No 1's or too many 1's
        if found_one == 0:
            incorrect_trains += 1
        # Wrong decision
        elif ytrain[u, value] == 0:
            incorrect_trains += 1


    if i % 10 == 0:
        data_plot(xtest, y_hat)
        test_error_rate = (incorrect_tests / number_test_inputs) * 100
        train_error_rate = (incorrect_trains / number_train_inputs) * 100
        print("Epoch %d Misclassified percentages" % i)
        print("Trained %d%%,\t Tested %d%%\n" % (train_error_rate, test_error_rate))

plt.ioff()
plt.show()
