from abc import ABC, abstractmethod

class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, population):
        pass