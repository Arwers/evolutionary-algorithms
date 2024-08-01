import numpy as np
from .chromosome import Chromosome


class Individual:
    def __init__(self, boundaries, precision, no_variables):
        self.genes = no_variables
        self.value = 0
        self.individual = np.array(
            [Chromosome(boundaries, precision) for _ in range(no_variables)]
        )

    def __str__(self):
        string_repr = ""
        for ind, chr in enumerate(self.get_individual()):
            string_repr += f"x[{ind}]: {chr.decode_chromosome()}\n"
        string_repr += f"Value: {self.get_value()}"
        return string_repr

    def get_size(self):
        return self.no_variables

    def get_individual(self):
        return self.individual

    def set_value(self, function):
        variables = [chr.decode_chromosome() for chr in self.get_individual()]
        self.value = function(*variables)

    def get_value(self):
        return self.value
