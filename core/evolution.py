import numpy as np
from .individual import Individual
from .chromosome import Chromosome
from .population import Population


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
    
    def evolve(self, selection, crossover, mutation):
        for generation in range(self.no_generations):
            self._evaluate_population()
            self._apply_selection(selection)
            self._apply_crossover(crossover)
            self._apply_mutation(mutation)
    
    def _evaluate_population(self):
        self.population.evaluate_population(self.function)
    
    def _apply_selection(self, selection):
        self.population.selection_population(selection)
    
    def _apply_crossover(self, crossover):
        self.population.crossover_population(crossover, crossover_rate=self.crossover_rate)
    
    def _apply_mutation(self, mutation):
        self.population.mutate_population(mutation, mutation_rate=self.mutation_rate)
