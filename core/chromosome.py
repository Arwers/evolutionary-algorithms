import numpy as np

class Chromosome:
    def __init__(self, size, boundaries):
        self._lower_bound = boundaries[0]
        self._upper_bound = boundaries[1]
        self._chromosome = np.zeros(size)

    def __str__(self):
        return f"chromosome: {self.get_binary_representation()}"

    def get_binary_representation(self):
        pass

    def get_decimal_representation(self):
        return self._chromosome