import numpy as np


class Perceptron(object):

    def __init__(self):
        self.w = np.random.randn(64) * 0.02
        self.b = np.random.randn(1) * 0.02

    def get_yhat(self, x):
        n, m = x.shape
        yhat = np.zeros(n,)
        for i in range(0, n, 1):
            computation = -self.b
            for j in range(0, m, 1):
                computation += self.w[j] * x[i, j]

            if computation >= 0:
                yhat[i] = 1
            else:
                yhat[i] = 0
        return yhat

    def train(self, input_x, goal_y, alpha):
        n, m = input_x.shape
        yhat = self.get_yhat(input_x)
        delta_w = np.zeros(m)
        delta_b = 0

        for i in range(0, n, 1):
            error = goal_y[i] - yhat[i]
            delta_w += error * input_x[i, :]
            delta_b -= error

        self.w += alpha * delta_w / float(n)
        self.b += alpha * delta_b / float(n)

        return self.w, self.b

    def get_weights(self):
        return self.w

    def get_bias(self):
        return self.b

