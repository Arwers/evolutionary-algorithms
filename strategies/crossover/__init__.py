from abc import ABC, abstractmethod

class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, population, crossover_rate):
        pass