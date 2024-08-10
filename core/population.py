import numpy as np
from .individual import Individual


class Population:
    def __init__(self, boundaries, precision, no_variables, pop_size):
        self.boundaries = boundaries
        self.precision = precision
        self.no_variables = no_variables
        self.pop_size = pop_size

        self.population = np.array(
            [Individual(boundaries, precision, no_variables) for _ in range(pop_size)]
        )

    def get_population(self):
        return self.population

    def evaluate_population(self, function):
        for individual in self.population:
            individual.set_value(function)

    def get_best(self):
        return min(self.population, key=lambda x: x.get_value())

    def get_mean(self):
        return np.mean([individual.get_value() for individual in self.population])
