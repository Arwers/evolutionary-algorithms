import numpy as np
from .individual import Individual

class Population:
    def __init__(self, boundaries, precision, no_variables, pop_size, elitism=True):
        self.boundaries = boundaries
        self.precision = precision
        self.no_variables = no_variables
        self.pop_size = pop_size
        self.elitism = elitism
        self.population = np.array([Individual(boundaries, precision, no_variables) for _ in range(pop_size)])

    def get_population(self):
        return self.population
    
    def set_population(self, population):
        set_population = np.array(population)

    def evaluate_population(self, function):
        for individual in self.population:
            individual.set_value(function)

    def apply_selection(self, selection_strategy):
        if self.elitism:
            best_individual = self.get_best()

        self.population = selection_strategy.select(self.population)

        if self.elitism:
            # Ensure the best individual(s) is/are retained
            worst_index = np.argmax([ind.get_value() for ind in self.population])
            self.population[worst_index] = best_individual

    def apply_crossover(self, crossover_strategy, crossover_rate):
        self.population = crossover_strategy.crossover(self.population, crossover_rate)

    def apply_mutation(self, mutation_strategy, mutation_rate):
        self.population = mutation_strategy.mutate(self.population, mutation_rate)

    def get_best(self):
        return min(self.population, key=lambda x: x.get_value())

    def get_mean(self):
        return np.mean([individual.get_value() for individual in self.population])