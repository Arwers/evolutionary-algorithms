from Mutation import MutationStrategy
from typing import List, Dict, Optional
from Core.individual import Individual
from Core.chromosome import Chromosome
import numpy as np


class EdgeMutation(MutationStrategy):
    def mutation(self, individual: Individual, mutation_rate: float) -> Individual:
        for chr in individual.get_binary_variables():
            flip_chance = np.random.random()
            if flip_chance < mutation_rate:
                gene_index = np.random.choice([0, chr.size() - 1])
                new_chr = chr.get_chromosome()
                new_chr[gene_index] = not new_chr[gene_index]
                chr.set_chromosome(new_chr)

        return individual