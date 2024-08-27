import numpy as np

from Crossover import CrossoverStrategy
from Core.individual import Individual
from Core.chromosome import Chromosome


class UniformCrossover(CrossoverStrategy):
    def crossover(self, ind_a: Individual, ind_b: Individual) -> tuple[Individual, Individual]:
        chromosomes_a = ind_a.get_binary_variables()
        chromosomes_b = ind_b.get_binary_variables()

        for i in range(len(chromosomes_a)):
            chr_a: Chromosome = chromosomes_a[i].get_chromosome()
            chr_b: Chromosome = chromosomes_b[i].get_chromosome()

            # Perform the crossover
            for j in range(chr_a.size):
                a = np.random.uniform(0, 1)
                if a < 0.5:
                    chr_a[j], chr_b[j] = chr_b[j], chr_a[j]

        return ind_a, ind_b