from typing import List, Dict
from Core.individual import Individual
from Selection import SelectionStrategy


class Best(SelectionStrategy):
    def selection(self, population: List[Individual], fitness_scores: List[float], sel_parameters: Dict) -> List[Individual]:
        # Pair fitness scores with individuals
        population_with_fitness = list(zip(fitness_scores, population))

        # Sort based on fitness scores in descending order
        sorted_population_with_fitness = sorted(
            population_with_fitness, key=lambda x: x[0], reverse=True
        )

        # Extract the sorted individuals
        sorted_population = [ind for _, ind in sorted_population_with_fitness]

        # Select top individuals based on fitness
        selection_size = int(sel_parameters["selection_size"] * len(population))
        selected_population = sorted_population[selection_size:]

        return selected_population
