import numpy as np

from Crossover import CrossoverStrategy
from Core.individual import Individual
from Core.chromosome import Chromosome


class TwoPointCrossover(CrossoverStrategy):
    def crossover(self, ind_a: Individual, ind_b: Individual) -> tuple[Individual, Individual]:
        chromosomes_a = ind_a.get_binary_variables()
        chromosomes_b = ind_b.get_binary_variables()

        for i in range(len(chromosomes_a)):
            chr_a: Chromosome = chromosomes_a[i].get_chromosome()
            chr_b: Chromosome = chromosomes_b[i].get_chromosome()

            points = np.sort(np.random.choice(range(1, chr_a.size), size=2, replace=False))
            # Perform the crossover
            new_chr_a = np.concatenate(
                (chr_a[:points[0]], chr_b[points[0]:points[1]], chr_a[points[1]:])
            )
            new_chr_b = np.concatenate(
                (chr_b[:points[0]], chr_a[points[0]:points[1]], chr_b[points[1]:])
            )

            # Set the new chromosomes
            chromosomes_a[i].set_chromosome(new_chr_a)
            chromosomes_b[i].set_chromosome(new_chr_b)

        return ind_a, ind_b