from abc import ABC, abstractmethod

class MutationStrategy(ABC):
    @abstractmethod
    def mutation(self):
        pass