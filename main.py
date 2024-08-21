from Core.chromosome import Chromosome
from Core.individual import Individual
from Core.population import Population
from Core.evolution import Evolution

from Fitness.parabola import Parabola
from Fitness.Levy import Levy
from Fitness.happycat import HappyCat
from Fitness.dejong_n5 import DeJongN5
from Fitness.styblinski_tang import StyblinskiTang

from Selection.best import Best

from Crossover.one_point import OnePointCrossover

from Mutation.one_point import OnePointMutation

import numpy as np
import random

def main():
    
    # Instantiate mutation and crossover strategies
    mutation_strategy = OnePointMutation()
    crossover_strategy = OnePointCrossover()
    fitness_function = Parabola()
    selection_strategy = Best()

    # Parameters for the population and individuals
    pop_parameters = {
        "gen_size": 50  # Population size
    }

    ind_parameters = {
        "boundaries": (-5, 5),  # Bounds for chromosome values
        "precision": 6,         # Decimal precision for chromosome
        "no_variables": fitness_function.get_no_variables(), # Number of variables
    }

    evo_parameters = {
        "generations": 50,     # Number of generations for the evolution
        "crossover_rate": 0.7,  # Crossover rate
        "mutation_rate": 0.01,   # Mutation rate
        "elitism": 0.1,        # Elitism rate (5% of the best individuals are preserved)
        "inversion_rate": 0.0,  # Inversion rate
    }

    sel_parameters = {
        "selection_size": 0.5  # Percentage of population to select
        # add parameters here for different selection strategies
        # e.g. "tournament_size": 5
        # Then get them by sel_parameters["tournament_size"]
    }
    
    # Create Evolution instance
    evolution = Evolution(
        ind_parameters=ind_parameters,
        pop_parameters=pop_parameters,
        evo_parameters=evo_parameters,
        sel_parameters=sel_parameters,
        fitness_function=fitness_function,
        mutation_strategy=mutation_strategy,
        crossover_strategy=crossover_strategy,
        selection_strategy=selection_strategy,
    )

    # Run the evolution process
    evolution.evolve()

    # save the results
    evolution.save_history("Results/levy.csv")

    # generate graphs
    evolution.plot_fitness()
    evolution.plot_standard_deviation()
    evolution.plot_mean()

if __name__ == "__main__":
    main()
