import numpy

import matplotlib.pyplot as plt


def display_color_matrix(color_matrix: numpy.ndarray, width=10):
    plt.imshow(numpy.tile(color_matrix, (width, 1, 1)))
    plt.show()
