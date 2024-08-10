from strategies.selection import SelectionStrategy


class SteadyStateSelection(SelectionStrategy):
    def __init__(self, percentage):
        self.percentage = percentage
    
    def select(self, population):
        population.evaluate_population()
        best_individuals = sorted(population, key=lambda x: x.get_value())[:int(len(population) * self.percentage)]
        population.set_population(best_individuals)