import random
from typing import List, Dict
from Core.individual import Individual
from Selection import SelectionStrategy


import random
from typing import List, Dict
from Core.individual import Individual
from Selection import SelectionStrategy

import random
from typing import List, Dict

import random
from typing import List, Dict

class Roulette(SelectionStrategy):
    def selection(self, population: List[Individual], fitness_scores: List[float], sel_parameters: Dict) -> List[Individual]:
        # Invert fitness scores to favor lower scores
        # Add a small constant to avoid division by zero
        inverted_fitness_scores = [1 / (score + 1e-10) for score in fitness_scores]
        
        # Calculate the total sum of inverted fitness scores
        total_fitness = sum(inverted_fitness_scores)

        # Calculate the probability of selection for each individual
        selection_probabilities = [score / total_fitness for score in inverted_fitness_scores]

        # Calculate cumulative probabilities
        cumulative_probabilities = []
        cumulative_sum = 0.0
        for prob in selection_probabilities:
            cumulative_sum += prob
            cumulative_probabilities.append(cumulative_sum)

        # Determine the number of individuals to select
        selection_size = int(sel_parameters["selection_size"] * len(population))
        selected_population = []

        for _ in range(selection_size):
            # Generate a random number in the range [0, 1)
            r = random.random()

            # Select the individual based on the random number
            for i, cumulative_prob in enumerate(cumulative_probabilities):
                if r < cumulative_prob:
                    selected_population.append(population[i])
                    break

        # Pair selected individuals with their fitness scores
        selected_with_fitness = [(ind, fitness_scores[population.index(ind)]) for ind in selected_population]

        # Sort the paired list by fitness scores (from lowest to highest)
        sorted_selected_with_fitness = sorted(selected_with_fitness, key=lambda x: x[1])

        # Extract and return the sorted individuals
        sorted_selected_population = [ind for ind, _ in sorted_selected_with_fitness]

        return sorted_selected_population
