from Mutation import MutationStrategy
from typing import List, Dict, Optional
from Core.individual import Individual
from Core.chromosome import Chromosome
import numpy as np


class TwoPointMutation(MutationStrategy):
    def mutation(self, individual: Individual, mutation_rate: float) -> Individual:
        for chr in individual.get_binary_variables():
            flip_chance = np.random.random()
            if flip_chance < mutation_rate:
                gene_indexex = np.random.choice(chr.size(), 2, replace=False)
                new_chr = chr.get_chromosome()
                for i in gene_indexex:
                    new_chr[i] = not new_chr[i]
                chr.set_chromosome(new_chr)

        return individual