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

# max num in list




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
def create_chromosome(num_gene):

    result_list = []
    for i in range(num_gene):
    # Generate first parameter: tuple of integer and float multiple of 0.5, between 0.5 and 20   
    # Generate first paramete     ====>    # address each tower


    int_param = random.uniform(1, 40) + 0.5
    float_param = random.uniform(0, 39.5) + 0.5
    first_param = (int_param, float_param)

    # Generate second parameter: list of integers, between 1 and 400, with random length
    # Generate second parameter:   ====> # The number of each neighborhood


    # second_param_len = random.randint(1, 400)   
    second_param_len = 5 # number of tower = 400 / num_nigbor   
    second_param = [random.randint(1, 400) for _ in range(second_param_len)]



    # Generate third parameter: decimal number, randomly selected from a list of possible values
    # Generate third parameter:    ====>  # bandwidth each tower  #  min_BW = 0.2 * 191932.0 = 38386.4 Max_BW = 3 * 191932.0 = 57589.6

    third_param_choices = [0.1, 0.2, 0.5, 1.0] 
    third_param = random.choice(third_param_choices)
    and_num = random.uniform(10, 200)

    # Append sublist to result list
    return result_list




def create_location_tower(num_gene):
    pass



        


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



# use https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6
def crossover_blend_BW(parent1, parent2, alpha=0.25):  # we use avg replace that
    """Perform crossover blend on two decimal numbers."""
    # Determine the blending point
    blend_point = random.uniform(0, 1)
    # Blend the parent values to create the offspring value
    offspring = alpha * parent1 + (1 - alpha) * parent2
    # Apply the blending factor to the offspring value
    offspring = (1 - blend_point) * parent1 + blend_point * offspring 
    return offspring

def crossover_blend_Blocks(parent1, parent2, alpha=0.25): # list type
    crossover_point = np.random.randint(len(parent1))
    offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return offspring1, offspring2


def crossover_blend_tower(parent1, parent2, alpha=0.25):  # tuple type
    parent1 = list(parent1)
    parent2 = list(parent2)
    sub = abs(parent1[0] - parent2[0])
    amount_of_change = alpha * sub
    
    if parent2[0] < parent1[0]:
        parent1[0] -= amount_of_change
    else:
        parent1[0] += amount_of_change

    if parent1[0] < parent2[0]:
        parent2[0] -= amount_of_change
    else:
        parent2[0] += amount_of_change

    if parent2[1] < parent1[1]:
        parent1[1] -= amount_of_change
    else:
        parent1[1] += amount_of_change
   
    if parent1[1] < parent2[1]:
        parent2[1] -= amount_of_change
    else:
        parent2[1] += amount_of_change
        
    offspring1 = (parent1[0], parent1[1])   
    offspring2 = (parent2[0], parent2[1])

    return offspring1, offspring2

    

def mutation_blend_BW():
    pass

def mutation_blend_Blocks():
    pass

def mutation_blend_tower():
    pass

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

numberOfTowers = random.randint(1, 40) # first time we use random tower number

for i in range(random.randint(1, 100)):
    for j in range(50):
        chromosome = create_chromosome(random.randint(1, 40))      
        fitness = fitness_function(chromosome)
        print(fitness)

