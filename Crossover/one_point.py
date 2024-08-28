import numpy as np

from Crossover import CrossoverStrategy
from Core.individual import Individual
from Core.chromosome import Chromosome


class OnePointCrossover(CrossoverStrategy):
    def crossover(self, ind_a: Individual, ind_b: Individual) -> tuple[Individual, Individual]:
        chromosomes_a = ind_a.get_binary_variables()
        chromosomes_b = ind_b.get_binary_variables()

        for i in range(len(chromosomes_a)):
            chr_a: Chromosome = chromosomes_a[i].get_chromosome()
            chr_b: Chromosome = chromosomes_b[i].get_chromosome()


            crossover_point = np.random.randint(0, chr_a.size)

            # Perform the crossover
            new_chr_a = np.concatenate(
                (chr_a[:crossover_point], chr_b[crossover_point:])
            )

            new_chr_b = np.concatenate(
                (chr_b[:crossover_point], chr_a[crossover_point:])
            )

            # Set the new chromosomes
            chromosomes_a[i].set_chromosome(new_chr_a)
            chromosomes_b[i].set_chromosome(new_chr_b)

        return ind_a, ind_b
