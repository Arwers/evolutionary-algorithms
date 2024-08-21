from Fitness import FitnessFunction
from Core.individual import Individual
import numpy as np

class DeJongN5(FitnessFunction):
    def __init__(self):
        self.no_variables = 2
    
    def fit(self, individual: Individual) -> float:
        # Decode the chromosome to get the x value
        x = individual.get_decimal_variables()
        x1 = x[0]
        x2 = x[1]
        total_sum = 0

        A = np.zeros((2, 25))
        a = np.array([-32, -16, 0, 16, 32])
        A[0, :] = np.tile(a, 5)
        ar = np.repeat(a, 5)
        A[1, :] = ar

        for ii in range(25):
            a1i = A[0, ii]
            a2i = A[1, ii]
            term1 = ii + 1
            term2 = (x1 - a1i)**6
            term3 = (x2 - a2i)**6
            new = 1 / (term1 + term2 + term3)
            total_sum += new

        y = 1 / (0.002 + total_sum)

        return y