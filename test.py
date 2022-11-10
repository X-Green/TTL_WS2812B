import numpy

import patterns

color_gen = patterns.PulseColorGenerator(
    cycle_length=100,
    base_color=numpy.array([255, 255, 255]),
    color_array_length=10,
    max_value=255,
    min_value=0
)

for i in range(200):
    print(color_gen.next_color_matrix())
