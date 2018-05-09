#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import time

plot_handles = []

x = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]]) # each row is an example
y = np.array([0,
              0,
              0,
              1]) # ideals

# randomly set the initial weight values and bias (last index of the weight vector
w = np.random.randn(3) * 0.03

epoch = 0
epoch_end = 2000


def perceptron_plot(x, y, w, b):
    global plot_handles

    I0 = np.where(y == 0)

    I1 = np.where(y == 1)

    x1s = np.array([-0.5, 1.5])
    x2s = (b-w[0]*x1s)/w[1]

    x_neg = (500 + b - w[0] * x1s)/w[1]

    if not plot_handles:
        plt.close('all')
        plt.figure()

        plt.ion()
        plt.show()

        plt.plot(x[I0, 0], x[I0, 1], 'r.')
        plt.plot(x[I1, 0], x[I1, 1], 'b.')

    for ph in plot_handles:
        ph.remove()

    plot_handles = []

    ph, = plt.plot(x1s, x2s, 'k-')

    plot_handles.append(ph)

    ph = plt.fill_between(x1s, x2s, x_neg, facecolor='blue', alpha=0.5)

    plot_handles.append(ph)

    plt.xlim([-0.5, 1.5])
    plt.ylim([-0.5, 1.5])

    plt.pause(0.1)
    time.sleep(0.1)


def hardlim(input):
    if input >= 0:
        return 1
    else:
        return 0


def hypothesis(input, weights):
    num_points, num_attributes = input.shape

    output = np.zeros(num_points,)

    for n in range (0, num_points, 1):
        activity = -weights[-1]

        for m in range (0, num_attributes, 1):
            activity += weights[m] * input[n,m]

        output[n] = hardlim(activity)

    return output


def learn(input, goal, weights, alpha):

    num_points, num_attributes = input.shape

    output = hypothesis(input, weights)

    delta_parameters = np.zeros((num_attributes+1,))

    for n in range(0, num_points, 1):
        error = goal[n] - output[n]
        delta_parameters[0:-1] += error * input[n, :]
        delta_parameters[-1] -= error

    weights += alpha * delta_parameters / float(num_points)

    return weights


for i in range(epoch_end):

    w = learn(x, y, w, 0.01)
    perceptron_plot(x, y, w, w[-1])



plt.ioff()
plt.show()
