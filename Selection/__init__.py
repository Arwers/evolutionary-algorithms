from abc import ABC, abstractmethod
from Core.individual import Individual
from typing import List

class SelectionStrategy(ABC):
    @abstractmethod
    def selection(self, population, fitness_scores, sel_params) -> List[Individual]:
        pass