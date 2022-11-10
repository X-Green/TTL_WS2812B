from abc import ABC, abstractmethod
import numpy
import colour


class ColorGenerator(ABC):
    @abstractmethod
    def next_color_matrix(self) -> numpy.ndarray:
        pass


class PulseColorGenerator(ColorGenerator):
    def __init__(self, cycle_length, color):
        pass

    def next_color_matrix(self) -> numpy.ndarray:
        pass
