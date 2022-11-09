import numpy
from numpy import array


def color_to_msg(rgb_matrix: numpy.ndarray):
    if rgb_matrix.shape[1] != 3:
        return None
    grb_matrix = rgb_matrix[:, [1, 0, 2]]

