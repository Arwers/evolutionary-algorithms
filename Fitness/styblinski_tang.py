from Fitness import FitnessFunction
from Core.individual import Individual
import numpy as np

class StyblinskiTang(FitnessFunction):
    def __init__(self):
        self.no_variables = 2
    
    def fit(self, individual: Individual) -> float:
        # Decode the chromosome to get the x value
        x = individual.get_decimal_variables()

        # Fitness function
        fitness = 0.5 * (np.sum(x**4) - 16 * np.sum(x**2) + 5 * np.sum(x))
        return fitness