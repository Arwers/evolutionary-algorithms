from Mutation import MutationStrategy
from typing import List, Dict, Optional
from Core.individual import Individual
from Core.chromosome import Chromosome
import numpy as np


class OnePointMutation(MutationStrategy):
    def mutation(self, individual: Individual, mutation_rate: float) -> Individual:
        binary_variables = individual.get_binary_variables()
        
        # Check if mutation should occur based on the mutation_rate
        if np.random.random() < mutation_rate:
            # Select a random chromosome
            chr = np.random.choice(binary_variables)
            
            # Select a random gene index within the chosen chromosome
            gene_index = np.random.randint(0, chr.size())
            
            # Get the current chromosome's binary sequence
            new_chr = chr.get_chromosome()
            
            # Flip the selected gene
            new_chr[gene_index] = not new_chr[gene_index]
            
            # Set the modified chromosome back
            chr.set_chromosome(new_chr)
            
            print(f"Gene at index {gene_index} in chromosome {chr} flipped")
        
        return individual

