#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import preprocessing

plot_handles = []

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

                if n >= num_points:
                    continue

                im = x[n, :].reshape(im_height, im_width)
                n += 1

                ph = figure_handle.add_subplot(4, 4, n)
                plot_handles.append(ph)

                ph.imshow(im)

                ph.xaxis.set_visible(False)
                ph.yaxis.set_visible(False)

    for n in range(len(plot_handles)):

        if np.sum(y[n,:]) != 1:
            class_label = "?"
        else:
            class_label = np.argmax(y[n,:])

        plot_handles[n].set_title(class_label)

    plt.pause(0.1)
    time.sleep(0.1)


digits = datasets.load_digits()
x = digits.data
y = digits.target

# im = x[n,:] if you wanted to select the nth image from the matrix, you select its nth row like so

y = np.expand_dims(y, axis=1)
enc = preprocessing.OneHotEncoder()
enc.fit(y)
y = enc.transform(y).toarray()

# im_label = y[n,:] if you wanted to select the label corresponding to the nth image, you can do it like this

# im_labels_7 = y[:,7] how to select the 7th column from matrix y

num_points, num_attributes = x.shape

I = np.random.permutation(num_points)

x = x[I, :]
y = y[I, :]

split = int(np.floor(num_points * 0.8))

xtrain = x[0:split, :]
ytrain = y[0:split, :]

xtest = x[split:, :]
ytest = y[split:, :]

W = np.random.normal(0, 1, (N, M))

