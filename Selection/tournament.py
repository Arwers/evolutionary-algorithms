import random
from typing import List, Dict
from Core.individual import Individual
from Selection import SelectionStrategy


class Tournament(SelectionStrategy):
    def selection(self, population: List[Individual], fitness_scores: List[float], sel_parameters: Dict) -> List[Individual]:
        tournament_size = sel_parameters.get("tournament_size", 3)
        selection_size = int(sel_parameters["selection_size"] * len(population))
        selected_population = []

        for _ in range(selection_size):
            # Randomly select individuals for the tournament
            tournament_indices = random.sample(range(len(population)), tournament_size)
            tournament_individuals = [population[i] for i in tournament_indices]
            tournament_fitnesses = [fitness_scores[i] for i in tournament_indices]

            # Choose the individual with the best (lowest) fitness
            best_individual_index = tournament_fitnesses.index(min(tournament_fitnesses))
            selected_population.append(tournament_individuals[best_individual_index])

        # Pair selected individuals with their fitness scores
        selected_with_fitness = [(ind, fitness_scores[population.index(ind)]) for ind in selected_population]

        # Sort the paired list by fitness scores (from lowest to highest)
        sorted_selected_with_fitness = sorted(selected_with_fitness, key=lambda x: x[1])

        # Extract and return the sorted individuals
        sorted_selected_population = [ind for ind, _ in sorted_selected_with_fitness]

        return sorted_selected_population
