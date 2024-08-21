from abc import ABC, abstractmethod

class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self):
        pass