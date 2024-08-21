from abc import ABC, abstractmethod
from Core.individual import Individual

class FitnessFunction(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    def get_no_variables(self):
        return self.no_variables
    
    @abstractmethod
    def fit(individual: Individual) -> float:
        pass