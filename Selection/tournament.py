from typing import List, Dict
from Core.individual import Individual
from Selection import SelectionStrategy


class Tournament(SelectionStrategy):
    def selection(self, population: List[Individual], fitness_scores: List[float], sel_parameters: Dict) -> List[Individual]:
        pass