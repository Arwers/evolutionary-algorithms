import numpy as np

from Crossover import CrossoverStrategy
from Core.individual import Individual
from Core.chromosome import Chromosome


class UniformCrossover(CrossoverStrategy):
    def crossover(self, ind_a: Individual, ind_b: Individual) -> tuple[Individual, Individual]:
        pass