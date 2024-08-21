from Fitness import FitnessFunction
from Core.individual import Individual
import numpy as np
import math

# f(x) = 2*x^2 + 5
class Levy(FitnessFunction):
    def __init__(self):
        self.no_variables = 2
    
    def fit(self, individual: Individual) -> float:
        # Decode the chromosome to get the x value
        x = individual.get_decimal_variables()
        
        # Fitness function
        fitness = np.sin(math.pi * (1 + (x[0] - 1) / 4))**2 + ((x[0] - 1) / 4)**2 * (1 + 10 * np.sin(math.pi * (1 + (x[0] - 1) / 4) + 1) ** 2) + ((x[1] - 1) / 4) ** 2 * (1 + np.sin(2 * math.pi * (1 + (x[1] - 1) / 4)) ** 2)
        return fitness