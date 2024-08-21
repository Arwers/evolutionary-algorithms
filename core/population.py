from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import numpy as np
import copy as cp

from Core.individual import Individual
from Mutation import MutationStrategy
from Crossover import CrossoverStrategy
from Fitness import FitnessFunction


class Population:
    """## Population class represents a population of individuals.\n
    The population is represented as a list of Individual instances.\n

    ### Parameters
    - **pop_parameters**: dictionary with the population parameters
    - **ind_parameters**: dictionary with the individual parameters
    - **ind_values**: list of Individual instances (optional)

    ### Attributes
    - **population**: list of Individual instances

    ### Methods
    - **get_population()**: Get the population
    - **set_population(new_population)**: Set the population
    - **mutation(mutation_rate, mutation_strategy)**: Apply mutation to the population
    - **crossover(crossover_rate, crossover_strategy)**: Apply crossover to the population
    - **get_size()**: Get the size of the population
    """

    def __init__(
        self,
        pop_parameters: Dict,
        ind_parameters: Dict,
        ind_values: Optional[List[Individual]] = None,
    ):
        self.pop_parameters = pop_parameters

        if ind_values is None:
            self.population = [
                Individual(
                    ind_parameters["boundaries"],
                    ind_parameters["precision"],
                    ind_parameters["no_variables"],
                )
                for _ in range(pop_parameters["gen_size"])
            ]
        else:
            self.population = ind_values

    def get_population(self) -> List[Individual]:
        return self.population

    def set_population(self, new_population: List[Individual]):
        # Ensure the new population contains only Individual instances
        if not all(isinstance(ind, Individual) for ind in new_population):
            raise ValueError(
                "All elements in new_population must be instances of Individual"
            )

        # Create deep copies of each Individual instance to avoid unintended side effects
        self.population = [cp.deepcopy(ind) for ind in new_population]

    def mutation(self, mutation_rate: float, mutation_strategy: MutationStrategy):
        new_population = []
        for ind in self.population:
            new_ind = mutation_strategy.mutation(ind, mutation_rate)
            new_population.append(new_ind)
        self.population = new_population

    def crossover(self, crossover_rate: float, crossover_strategy: CrossoverStrategy):
        new_population = []

        # Iterate over pairs
        while len(new_population) < self.pop_parameters["gen_size"]:
            index_a = np.random.randint(0, len(self.population))
            index_b = np.random.randint(0, len(self.population))
            crossover_chance = np.random.random()

            if crossover_chance < crossover_rate:
                ind_a, ind_b = crossover_strategy.crossover(
                    self.population[index_a], self.population[index_b]
                )
                new_population.append(ind_a)
                new_population.append(ind_b)
            else:
                new_population.append(self.population[index_a])
                new_population.append(self.population[index_b])

        self.population = new_population

    def get_size(self) -> int:
        return len(self.population)
