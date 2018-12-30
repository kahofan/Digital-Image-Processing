# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:41:42 2018

@author: Lionel
"""

from matplotlib import pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot = False)
x_train = mnist.train._images
y_train = mnist.train._labels

fig, ax = plt.subplots(
        nrows = 2,
        ncols = 5,
        sharex = True,
        sharey = True)
ax = ax.flatten()
for i in range(10):
    img = x_train[y_train == i][0].reshape(28, 28)
    ax[i].imshow(img, cmap = 'Greys', interpolation = 'nearest')
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
