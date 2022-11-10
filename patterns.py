from abc import ABC, abstractmethod
import numpy
import colour


class ColorGenerator(ABC):
    @abstractmethod
    def next_color_matrix(self) -> numpy.ndarray:
        pass


class PulseColorGenerator(ColorGenerator):
    def __init__(self, cycle_length, base_color: numpy.ndarray, color_array_length, max_value=255, min_value=0):
        self.cycle_length = cycle_length
        self.base_color = base_color.astype(numpy.uint8)
        self.max_val = max_value
        self.min_val = min_value
        self.length = color_array_length

        self.in_cycle_progress = 0

    def next_color_matrix(self) -> numpy.ndarray:
        self.in_cycle_progress += 1
        if self.in_cycle_progress > self.cycle_length:
            self.in_cycle_progress = 0
        gamma = abs(self.in_cycle_progress * 2 - self.cycle_length) / self.cycle_length
        color_new = (self.base_color * gamma).astype(numpy.uint8)
        return numpy.tile(color_new, (self.length, 1))
