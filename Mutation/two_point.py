from Mutation import MutationStrategy
from typing import List, Dict, Optional
from Core.individual import Individual
from Core.chromosome import Chromosome
import numpy as np


class TwoPointMutation(MutationStrategy):
    def mutation(self, individual: Individual, mutation_rate: float) -> Individual:
        pass