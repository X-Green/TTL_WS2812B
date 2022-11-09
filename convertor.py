import numpy
from numpy import array


def color_to_bit_array(rgb_matrix: numpy.ndarray):
    if rgb_matrix.shape[1] != 3:
        return None
    rgb_matrix = rgb_matrix.astype(dtype=numpy.uint8)
    grb_matrix = rgb_matrix[:, [1, 0, 2]]
    color_byte_array = grb_matrix.reshape(-1)
    return numpy.unpackbits(color_byte_array, bitorder='big')


def color_bit_array_to_msg_bytes():
    pass


if __name__ == "__main__":
    print(color_to_bit_array(array(
        [
            [0xFF, 0xFF, 0xFF],
            [0xAF, 0xBF, 0xCF],
            [0x0F, 0x1F, 0x2F],
            [0x3F, 0x4F, 0x5F],
        ]
    )))
