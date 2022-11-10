import numpy
from numpy import array

import test_legacy


def color_to_bit_array(rgb_matrix: numpy.ndarray):
    if rgb_matrix.shape[1] != 3:
        raise Exception("Input ndarray should be of shape(n, 3)")
    rgb_matrix = rgb_matrix.astype(dtype=numpy.uint8)
    grb_matrix = rgb_matrix[:, [1, 0, 2]]
    color_byte_array = grb_matrix.reshape(-1)
    return numpy.unpackbits(color_byte_array, bitorder='big')


def color_bit_array_to_msg_bytes(color_bit_array: numpy.ndarray):
    color_bit_matrix = color_bit_array.reshape(-1, 3).T
    uart_mask = 0b0100100
    msg_byte_array = (color_bit_matrix[2] << 6) | (color_bit_matrix[1] << 3) | color_bit_matrix[0] | uart_mask
    msg_byte_array_inverted = numpy.bitwise_not(msg_byte_array) & 0x7F
    return msg_byte_array_inverted


if __name__ == "__main__":
    # test
    source = array(
        [
            [0xEA, 0b01101011, 0x0D],
            [0xAF, 0xBF, 0xCF],
            [0x0F, 0x1F, 0x2F],
            [0x3F, 0x4F, 0x5F],
        ]
    )
    print(color_bit_array_to_msg_bytes(
        color_to_bit_array(
            source
        )
    ))

    print(test_legacy.colorToMessage(source[0]))
