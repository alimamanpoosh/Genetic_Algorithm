import numpy as np
import random
# Define the problem parameters
num_neighborhoods = 400
min_speed = 0.2  # megabit
list_speed = [0, 0.2, 1, 3] 
Satisfactionـscore = [0,10,20,40]
max_cost = 10000  # arbitrary cost limit
speed_weights = 0.2
cost_weights = 0.8

# def read problem_config.json file and save in the dictionary




def nominal_bandwidth(Bw_ty, bj, blocks):
    return Bw_ty * bj / sum(blocks)
    

def COV(x,y):
    sigma_inverted = [[1/8, 0], [0, 1/8]]

    X = np.array(x)
    Y = np.array(y)

    subtract = np.subtract(X, Y)

    return np.exp(-0.5*(subtract) * sigma_inverted * np.transpose(subtract))
    

def real_bandwidth(Bw_ty, bj, blocks, x, y):
    bw_prime = nominal_bandwidth(Bw_ty, bj, blocks)
    cov = COV(x, y)
    return cov * bw_prime



# This function calculates the total population of the neighborhood
def calculate_population():  
    with open('blocks_population.txt') as f:
        lines = f.read().splitlines()

    neighborPopulation = []
    for i in lines:
        neighborPopulation.extend(i.split(','))

    result = np.array(neighborPopulation, dtype=int)
    totalPopulation = np.sum(result)
    return totalPopulation

# Define the chromosome representation
def create_chromosome(num_gene, num_lists):
    param1_range = range(0, 400)  # address each tower
    param2_range = range(1, 400)  # The number of each neighborhood
    param3_range = range(1, 6)  # bandwidth each tower  #  min_BW = 0.2 * 191932.0 = 38386.4 Max_BW = 3 * 191932.0 = 57589.6
    
    # num_lists = 5 # Define the number of internal lists you want to create
    chromosome = []
    for i in range(num_lists):
        internal_list = [random.choice(param1_range),
                         random.choice(param2_range),
                         random.choice(param3_range)]
        chromosome.append(internal_list)
    return chromosome
    

    
        


# Define the fitness function
def fitness_function(chromosome):
    # Calculate the cost and speed of the solution
    cost = np.sum(chromosome) * max_cost / num_neighborhoods
    # speed = np.sum(chromosome) * min_speed

    for i in list_speed:
        speed = np.sum(chromosome) * list_speed[i]


    # Calculate the fitness as a weighted sum of cost and speed
    fitness = cost_weights * cost + speed_weights * speed[0]
    for i in range(len(list_speed)):
        temp = cost_weights * cost + speed_weights * speed[i]
        fitness = min(temp, fitness)

    return fitness


# Define the genetic operators
def mutation(chromosome, mutation_rate=0.01):
    for i in range(len(chromosome)):
        if np.random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # flip the bit  1==> 0 and 0==>1
    return chromosome


def crossover(parent1, parent2): #genrate offspring from parent
    crossover_point = np.random.randint(len(parent1))
    offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return offspring1, offspring2


# Implement the evolutionary algorithm
# population_size = 100
population_size = calculate_population()
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


for i in range(random.randint(1, 100)):
    for j in range(50):
        create_chromosome()
        Num_gene = random.randint(1, 40)
        chromosome = []
        for i in 
        

