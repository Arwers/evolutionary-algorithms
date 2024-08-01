import numpy as np
from .chromosome import Chromosome

class Individual:
    def __init__(self, genes, boundaries, precision):
        self.genes = genes
        self.individual = np.array([Chromosome(boundaries, precision) for _ in range(genes)])
    
    def __str__(self):
        string_repr = ""
        for chr in self.get_individual():
            string_repr += f"{chr.decode_chromosome()}\n"
        return string_repr
            

    def get_size(self):
        return self.genes
    
    def get_individual(self):
        return self.individual