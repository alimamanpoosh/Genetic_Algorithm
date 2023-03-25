import numpy as np

# Define the problem parameters
num_neighborhoods = 400
min_speed = 0.2  # megabit
list_speed = [0.2, 1, 3]
max_cost = 10000  # arbitrary cost limit
speed_weights = 0.2
cost_weights = 0.8




def calculate_population():  # This function calculates the total population of the neighborhood
    with open('blocks_population.txt') as f:
        lines = f.read().splitlines()

    neighborPopulation = []
    for i in lines:
        neighborPopulation.extend(i.split(','))

    result = np.array(neighborPopulation, dtype=int)
    totalPopulation = np.sum(result)
    return totalPopulation


totalPopulationCity = calculate_population()


# Define the chromosome representation
def create_chromosome():
    return np.random.randint(2, size=num_neighborhoods)


# Define the fitness function
def fitness_function(chromosome):
    # Calculate the cost and speed of the solution
    cost = np.sum(chromosome) * max_cost / num_neighborhoods
    speed = np.sum(chromosome) * min_speed

    # Calculate the fitness as a weighted sum of cost and speed
    fitness = cost_weights * cost + speed_weights * speed

    return fitness


# Define the genetic operators
def mutation(chromosome, mutation_rate=0.01):
    for i in range(len(chromosome)):
        if np.random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # flip the bit
    return chromosome


def crossover(parent1, parent2):
    crossover_point = np.random.randint(len(parent1))
    offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return offspring1, offspring2


# Implement the evolutionary algorithm
population_size = 100
mutation_rate = 0.01
num_generations = 100

population = [create_chromosome() for i in range(population_size)]
for generation in range(num_generations):
    # Evaluate the fitness of the population
    fitness = [fitness_function(chromosome) for chromosome in population]

    # Select the parents for the next generation
    parents_indices = np.random.choice(range(population_size), size=2, replace=False, p=fitness / np.sum(fitness))
    parent1 = population[parents_indices[0]]
    parent2 = population[parents_indices[1]]

    # Generate the offspring for the next generation
    offspring1, offspring2 = crossover(parent1, parent2)
    offspring1 = mutation(offspring1, mutation_rate)
    offspring2 = mutation(offspring2, mutation_rate)

    # Replace the least fit individuals with the offspring
