import numpy as np
from ..population.population import Population

class Evolution:
    def __init__(self, boundaries, precision, no_variables, no_individuals, 
                 no_generations, function, mutation_rate, crossover_rate, elitism=True):
        self.boundaries = boundaries
        self.precision = precision
        self.no_variables = no_variables
        self.no_individuals = no_individuals
        self.no_generations = no_generations
        self.function = function
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism
        self.population = Population(boundaries, precision, no_variables, no_individuals, elitism)
    
    def evolve(self, selection_strategy, crossover_strategy, mutation_strategy):
        for generation in range(self.no_generations):
            # Evaluate population
            self.population.evaluate_population(self.function)
            
            # Apply selection strategy
            self.population.apply_selection(selection_strategy)
            
            # Apply crossover strategy
            self.population.apply_crossover(crossover_strategy, crossover_rate=self.crossover_rate)
            
            # Apply mutation strategy
            self.population.apply_mutation(mutation_strategy, mutation_rate=self.mutation_rate)

    def get_best_individual(self):
        return self.population.get_best()

    def get_population_mean(self):
        return self.population.get_mean()