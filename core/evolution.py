from typing import Dict, Callable, List
import numpy as np
import copy as cp
from Core.chromosome import Chromosome
from Core.individual import Individual
from Core.population import Population
from Mutation import MutationStrategy
from Crossover import CrossoverStrategy
from Selection import SelectionStrategy
from Fitness import FitnessFunction
from matplotlib import pyplot as plt


class Evolution:
    """## Evolution class is responsible for the evolution process.\n
    The evolution process consists of the following steps:
    - Evaluate the fitness of the current population
    - Select individuals for reproduction
    - Apply elitism (if configured)
    - Generate new population through crossover
    - Apply mutation
    - Integrate elite individuals back into the population
    - Re-evaluate fitness after the final population is formed
    - Track the best individual and fitness in the current generation
    - Repeat for the specified number of generations

    ### Parameters
    - **ind_parameters**: dictionary with parameters for the individuals
    - **pop_parameters**: dictionary with parameters for the population
    - **evo_parameters**: dictionary with parameters for the evolution process
    - **sel_parameters**: dictionary with parameters for the selection process
    - **fitness_function**: instance of the FitnessFunction class
    - **mutation_strategy**: instance of the MutationStrategy class
    - **crossover_strategy**: instance of the CrossoverStrategy class
    - **selection_strategy**: instance of the SelectionStrategy class

    ### Attributes
    - **population**: instance of the Population class
    - **history**: list of tuples with the best fitness and individual in each generation
    (generation, best_fitness, best_individual)

    """

    def __init__(
        self,
        ind_parameters: Dict,
        pop_parameters: Dict,
        evo_parameters: Dict,
        sel_parameters: Dict,
        fitness_function: FitnessFunction,
        mutation_strategy: MutationStrategy,
        crossover_strategy: CrossoverStrategy,
        selection_strategy: SelectionStrategy,
    ):
        self.ind_parameters = ind_parameters
        self.pop_parameters = pop_parameters
        self.evo_parameters = evo_parameters
        self.sel_parameters = sel_parameters
        self.elitism = True if evo_parameters["elitism"] > 0 else False

        self.fitness_function = fitness_function
        self.mutation_strategy = mutation_strategy
        self.crossover_strategy = crossover_strategy
        self.selection_strategy = selection_strategy

        # Initialize the population
        self.population = Population(pop_parameters, ind_parameters)

        # Track evolution progress
        self.history = []

    def evaluate_fitness(self):
        fitness_scores = [
            float(self.fitness_function.fit(ind))
            for ind in self.population.get_population()
        ]
        return fitness_scores
    
    def inversion(self):
        """Inverts the chromosomes of an individual."""
        for individual in self.population.get_population():
            for chromosome in individual.get_binary_variables():
                chance = np.random.rand()
                if chance > self.evo_parameters["inversion_rate"]:
                    point_a = np.random.randint(0, chromosome.size())
                    point_b = np.random.randint(point_a, chromosome.size())

                    flipped_chromosome = chromosome.get_chromosome()
                    flipped_chromosome[point_a:point_b] = flipped_chromosome[point_a:point_b][::-1]
                    chromosome.set_chromosome(flipped_chromosome)

    def save_history(self, filename: str):
        with open(filename, "w") as file:
            file.write("generation,best_fitness,best_individual,std,mean\n")
            for generation, best_fitness, best_individual, std, mean in self.history:
                file.write(
                    f"{generation},{best_fitness},{1}, {std}, {mean}\n")
                
    def plot_fitness(self) -> List:
        generations = [gen for gen, _, _, _, _ in self.history]
        fitness = [fit for _, fit, _, _, _ in self.history]
        plt.plot(generations, fitness)
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title("Fitness over Generations")
        plt.show()

    def plot_standard_deviation(self) -> List:
        generations = [gen for gen, _, _, _, _ in self.history]
        std = [std for _, _, _, std, _ in self.history]
        plt.plot(generations, std)
        plt.xlabel("Generation")
        plt.ylabel("Standard Deviation")
        plt.title("Standard Deviation over Generations")
        plt.show()
        
    def plot_mean(self) -> List:
        generations = [gen for gen, _, _, _, _ in self.history]
        mean = [mean for _, _, _, _, mean in self.history]
        plt.plot(generations, mean)
        plt.xlabel("Generation")
        plt.ylabel("Mean")
        plt.title("Mean over Generations")
        plt.show()

    def evolve(self):
        all_time_best_fitness = float("inf")
        all_time_best_individual = None

        for generation in range(self.evo_parameters["generations"]):
            print(f"Generation {generation + 1}")

            # Evaluate fitness of the current population
            fitness_scores = self.evaluate_fitness()

            # Selection process (Note: the selected population should be sorted by fitness)
            selected_population = self.selection_strategy.selection(
                self.population.get_population(), fitness_scores, self.sel_parameters
            )

            # Apply elitism: preserve the best individuals after selection
            if self.elitism:
                elite_count = int(self.evo_parameters["elitism"] * len(selected_population))
                curr_size = len(selected_population)
                elite_individuals = [
                    cp.deepcopy(selected_population[curr_size - i - 1])
                    for i in range(elite_count)
                ]

            # Replace the population with selected individuals (excluding elites)
            self.population.set_population(selected_population)

            # Generate new population through crossover
            self.population.crossover(
                self.evo_parameters["crossover_rate"], self.crossover_strategy
            )

            # Apply mutation
            self.population.mutation(
                self.evo_parameters["mutation_rate"], self.mutation_strategy
            )

            # Inversion
            self.inversion()

            # Integrate the elite individuals back into the population after mutation
            if self.elitism:
                self.population.set_population(
                    np.concatenate(
                        (self.population.get_population()[elite_count:], elite_individuals)
                    )
                )

            # Re-evaluate fitness after the final population is formed
            fitness_scores = self.evaluate_fitness()

            # Track the best individual and fitness in the current generation
            best_fitness = float("inf")
            best_individual = None

            # Iterate through individuals and their fitness scores to find the best one
            for i, fitness in enumerate(fitness_scores):
                current_individual = self.population.get_population()[i]
                if fitness < best_fitness:  # Since we are minimizing
                    best_fitness = fitness
                    best_individual = current_individual

                # Check if this is the best individual we've seen across all generations
                if fitness < all_time_best_fitness:
                    all_time_best_fitness = fitness
                    all_time_best_individual = cp.deepcopy(current_individual)

            # Store snapshot of the best individual in this generation
            gen_std = np.std(fitness_scores)
            gen_mean = np.mean(fitness_scores)
            self.history.append((generation + 1, best_fitness, best_individual, gen_std, gen_mean))

            print(f"Best fitness in generation {generation + 1}: {best_fitness}")
            print(
                f"Best individual in generation {generation + 1}: {best_individual.get_decimal_variables()}"
            )
        print(f"All time best fitness: {all_time_best_fitness}")
        print(
            f"All time best individual: {all_time_best_individual.get_decimal_variables()}"
        )
