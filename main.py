import core.chromosome
import core.individual
import core.population

def main():
    pop = core.population.Population((-5,5), 6, 2, 5)
    pop.evaluate_population(lambda x, y: x + y)
    for ind in pop.get_population():
        print(ind)

    print()
    print(f"Best: \n {pop.get_best()} \n")    
    print(f"Mean: \n {pop.get_mean()}")
if __name__ == "__main__":
    main()