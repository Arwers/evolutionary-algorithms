import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Core.evolution import Evolution
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
from Selection.roulette import Roulette
from Selection.tournament import Tournament

from Crossover.one_point import OnePointCrossover
from Crossover.two_point import TwoPointCrossover
from Crossover.three_point import ThreePointCrossover
from Crossover.uniform import UniformCrossover
from Crossover.discrete import DiscreteCrossover

from Mutation.one_point import OnePointMutation
from Mutation.two_point import TwoPointMutation
from Mutation.edge import EdgeMutation


def setup(
    function,
    lower_bound,
    upper_bound,
    precision,
    population_size,
    generations,
    selection,
    crossover,
    crossover_rate,
    mutation,
    mutation_rate,
    elitism,
    inverse,
    tournament_size,
    selection_size,
):
    mutation_strategy = None
    crossover_strategy = None
    fitness_function = None
    selection_strategy = None
    pop_parameters = {}
    ind_parameters = {}
    evo_parameters = {}
    sel_parameters = {}

    if mutation == "One Point":
        mutation_strategy = OnePointMutation()
    elif mutation == "Two Point":
        mutation_strategy = TwoPointMutation()
    elif mutation == "Edge":
        mutation_strategy = EdgeMutation()

    if crossover == "One Point":
        crossover_strategy = OnePointCrossover()
    elif crossover == "Two Point":
        crossover_strategy = TwoPointCrossover()
    elif crossover == "Three Point":
        crossover_strategy = ThreePointCrossover()
    elif crossover == "Uniform":
        crossover_strategy = UniformCrossover()
    elif crossover == "Discrete":
        crossover_strategy = DiscreteCrossover()

    if selection == "Best":
        selection_strategy = Best()
    elif selection == "Roulette":
        selection_strategy = Roulette()
    elif selection == "Tournament":
        selection_strategy = Tournament()

    if function == "Parabola":
        fitness_function = Parabola()
    elif function == "DeJong N.5":
        fitness_function = DeJongN5()
    elif function == "Levy":
        fitness_function = Levy()
    elif function == "Styblinski-Tang":
        fitness_function = StyblinskiTang()
    elif function == "HappyCat":
        fitness_function = HappyCat()

    if selection == "Tournament":
        sel_parameters["tournament_size"] = tournament_size
    elif selection == "Roulette":
        sel_parameters["roulette_selection_size"] = selection_size
    elif selection == "Best":
        sel_parameters["selection_size"] = selection_size

    pop_parameters = {
        "gen_size": population_size
    }

    ind_parameters = {
        "boundaries": (lower_bound, upper_bound),
        "precision": precision,
        "no_variables": fitness_function.get_no_variables(),
    }

    evo_parameters = {
        "generations": generations,
        "crossover_rate": crossover_rate,
        "mutation_rate": mutation_rate,
        "elitism": elitism,
        "inversion_rate": inverse,
    }

    sel_parameters = {
        "selection_size": selection_size
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
    result = evolution.evolve()
    evolution.save_history("Results/result.csv")
    evolution.plot_fitness()
    evolution.plot_standard_deviation()
    evolution.plot_mean()

    return result
