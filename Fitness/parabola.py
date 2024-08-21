from Fitness import FitnessFunction
from Core.individual import Individual

# f(x) = 2*x^2 + 5
class Parabola(FitnessFunction):
    def __init__(self):
        self.no_variables = 1
    
    def fit(self, individual: Individual) -> float:
        # Decode the chromosome to get the x value
        x_values = individual.get_decimal_variables()
        
        # Fitness function
        fitness = 2 * sum(x**2 for x in x_values) + 5
        return fitness