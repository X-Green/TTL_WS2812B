"""
color_gen = patterns.PulseColorGenerator(
    cycle_length=100,
    base_color=numpy.array([255, 255, 255]),
    color_array_length=10,
    max_value=255,
    min_value=0
)

for i in range(200):
    print(color_gen.next_color_matrix())
"""
import numpy

import previer_helper

if __name__ == "__main__":
    previer_helper.display_color_matrix(numpy.arange(0, 210).repeat(3).reshape(-1, 3))
