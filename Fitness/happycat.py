from Fitness import FitnessFunction
from Core.individual import Individual
import numpy as np
import math

class HappyCat(FitnessFunction):
    def __init__(self):
        self.no_variables = 2
    
    def fit(self, individual: Individual) -> float:
        # Decode the chromosome to get the vector x
        x = individual.get_decimal_variables()
        
        # Ensure x has the correct number of variables
        if len(x) != self.no_variables:
            raise ValueError(f"Expected {self.no_variables} variables, got {len(x)}.")
        
        # Compute the squared Euclidean norm of the vector x
        norm_x_sq = np.sum(x ** 2)
        
        # Parameters for the HappyCat function
        alpha = 0.125
        n = self.no_variables
        
        # Fix: Use absolute value to avoid complex number issues
        term1 = np.abs(norm_x_sq - n) ** (2 * alpha)
        term2 = (0.5 * norm_x_sq + np.sum(x)) / n
        fitness = term1 + term2 + 0.5
        
        return fitness