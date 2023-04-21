import numpy as np
import random
import json
from operator import itemgetter
import copy

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the problem parameters
num_neighborhoods = 400
first_neighbor_location = (0.5, 0.5)
min_speed = 0.2  # megabit
list_speed = [0.2, 1, 3]
max_cost = 10000  # arbitrary cost limit
speed_weights = 0.2
cost_weights = 0.8
crossover_rate = 0.9
mutation_rate = 0.1
totalPopulation = 0
dict_neighborhood = {}

location = 'location'
blocks = 'blocks'
BW = 'BW'
totoal_city_list = []
chart_fitness = []


# read problem_config.json file and save in the dictionary
with open('/content/drive/MyDrive/Colab Notebooks/CI_P1/problem_config.json') as f:
    data = json.load(f)
tower_construction_cost = data.get('tower_construction_cost')
tower_maintanance_cost = data.get('tower_maintanance_cost')
user_satisfaction_levels = data.get('user_satisfaction_levels')
user_satisfaction_scores = data.get('user_satisfaction_scores')


# This function calculates the total population of the neighborhood

def calculate_population():
    with open('/content/drive/MyDrive/Colab Notebooks/CI_P1/blocks_population.txt') as f:
        lines = f.read().splitlines()

    neighbor_population = []
    for i in lines:
        neighbor_population.extend(i.split(','))

    result = np.array(neighbor_population, dtype=int)
    global totalPopulation
    for i in range(400):
        dict_neighborhood[i] = result[i]
        totalPopulation += result[i]


# Define the chromosome representation
def create_chromosome(num_of_gens):
    chromosome = []
    n = 400 // num_of_gens
    rand = random.sample(range(0, 400), 400)
    for i in range(num_of_gens):
        gen = dict()
        x = 0
        if first_neighbor_location[0] == 0:
            x = random.uniform(0, 20)
        elif first_neighbor_location[0] == 0.5:
            x = random.uniform(0.5, 20.5)
        y = 0
        if first_neighbor_location[0] == 0:
            y = random.uniform(0, 20)
        elif first_neighbor_location[0] == 0.5:
            y = random.uniform(0.5, 20.5)

        gen[location] = (x, y)

        gen[blocks] = [j for j in rand[i * n:n * (i + 1)]]

        population = 0
        for b in gen[blocks]:
            population += dict_neighborhood[b]
        gen[BW] = random.uniform(0, 3 * population)

        chromosome.append(gen)

    return chromosome


def nominal_bandwidth(bw_ty, bj, blocks):
    pop = 0
    for b in blocks:
        pop += dict_neighborhood[b]

    return dict_neighborhood[bj] * bw_ty / pop


def cov(x, y):
    sigma_inverted = np.array([[1 / 8, 0], [0, 1 / 8]])

    X = np.array(x)
    Y = np.array(y)

    subtract = np.subtract(X, Y)

    return np.exp(-0.5 * (subtract) @ sigma_inverted @ np.transpose(subtract))


# Define the fitness function
def fitness(chromosome):
    fit = 0
    for gen in (chromosome):
        total = 0
        for b in gen[blocks]:
            block_x = b % 20 + first_neighbor_location[0]
            block_y = int(b / 20) + first_neighbor_location[1]

            bw_prime = nominal_bandwidth(gen[BW], b, gen[blocks])
            bw_block = cov(gen[location], (block_x, block_y)) * bw_prime
            bw_user = bw_block / dict_neighborhood[b]

            u_score = 0
            for i in range(len(user_satisfaction_levels)):
                if bw_user < user_satisfaction_levels[i]:
                    u_score = user_satisfaction_scores[i]
                    break
                if i == 2:
                    u_score = user_satisfaction_scores[3]

            b_score = u_score * dict_neighborhood[b]
            cost = tower_construction_cost + tower_maintanance_cost * gen[BW]

            total += (b_score - cost)

        fit += total

    return fit


def crossover_blocks(parent1, parent2):
    crossover_point = int(random.uniform(0, 1) * len(parent1))
    p = random.randint(0, 1)
    if p == 0:
        offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
        offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    else:
        offspring1 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
        offspring2 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])

    return offspring1.tolist(), offspring2.tolist()


def crossover_tower(parent1, parent2, alpha=0.25):  # tuple type
    parent1 = list(parent1)
    parent2 = list(parent2)
    sub = abs(parent1[0] - parent2[0])
    amount_of_change_x = alpha * sub
    amount_of_change_y = alpha * abs(parent1[1] - parent2[1])

    if parent2[0] < parent1[0]:
        parent1[0] -= amount_of_change_x
        parent2[0] += amount_of_change_x
    else:
        parent1[0] += amount_of_change_x
        parent2[0] -= amount_of_change_x

    if parent2[1] < parent1[1]:
        parent1[1] -= amount_of_change_y
        parent2[1] += amount_of_change_y
    else:
        parent1[1] += amount_of_change_y
        parent2[1] -= amount_of_change_y

    offspring1 = (parent1[0], parent1[1])
    offspring2 = (parent2[0], parent2[1])

    return offspring1, offspring2


def crossover_BW(parent1, parent2, alpha=0.25):  # we use avg replace that
    # parent1 ===>  gen 1
    # parent2 ===>  gen 2

    # """Perform crossover blend on two decimal numbers."""
    d = abs(parent1 - parent2)
    result0 = random.uniform(parent1 - alpha * d, parent2 + alpha * d)
    result1 = random.uniform(parent1 - alpha * d, parent2 + alpha * d)

    result2 = random.uniform(parent2 - alpha * d, parent1 + alpha * d)
    result3 = random.uniform(parent2 - alpha * d, parent1 + alpha * d)

    
    if parent2 > parent1:
        if result0 < 0 and result1 < 0:
            return (72, 72)
        elif result0< 0 and result1 > 0:
            return (72, result1)
        elif result0 > 0 and result1 < 0:
            return (result0, 72)
        else:
            return (result0, result1)
        # return random.uniform(parent1 - alpha * d, parent2 + alpha * d), random.uniform(parent1 - alpha * d, parent2 + alpha * d)
    else:
        if result2 < 0 and result3 < 0:
            return (72, 72)
        elif result2 < 0 and result3 > 0:
            return (72, result3)
        elif result2 > 0 and result3 < 0:
            return (result2, 72)
        else:
            return (result2, result3)

# def crossover_BW(parent1, parent2, alpha=0.25):  # we use avg replace that
#     # parent1 ===>  gen 1
#     # parent2 ===>  gen 2

#     # """Perform crossover blend on two decimal numbers."""
#     d = abs(parent1 - parent2)
#     if parent2 > parent1:
#         return random.uniform(parent1 - alpha * d, parent2 + alpha * d), random.uniform(parent1 - alpha * d,
#                                                                                         parent2 + alpha * d)
#     return random.uniform(parent2 - alpha * d, parent1 + alpha * d), random.uniform(parent2 - alpha * d,
#                                                                                     parent1 + alpha * d)

def crossover(chro1, chro2):
    child1, child2 = copy.deepcopy(chro1), copy.deepcopy(chro2)
    for i in range(len(child1)):
        child1[i][blocks], child2[i][blocks] = crossover_blocks(child1[i][blocks], child2[i][blocks])

        for j in range(len(child1[i][blocks])):
            for gen1, gen2 in zip(chro1, chro2):
                if gen1 is not child1[i]:
                    if child1[i][blocks][j] in gen1[blocks]:
                        gen1[blocks] = list(gen1[blocks])
                        k = gen1[blocks].index(child1[i][blocks][j])
                        gen1[blocks][k] = child2[i][blocks][j]

                if gen2 is not child2[i]:
                    if child2[i][blocks][j] in gen2[blocks]:
                        gen2[blocks] = list(gen2[blocks])
                        k = gen2[blocks].index(child2[i][blocks][j])
                        gen2[blocks][k] = child1[i][blocks][j]

        child1[i][location], child2[i][location] = crossover_tower(child1[i][location], child2[i][location])

        child1[i][BW], child2[i][BW] = crossover_BW(child1[i][BW], child2[i][BW])

    return child1, child2


def mutation_bw(parent1):  # parent decimal number
    multi_neighborhood_population = sum([dict_neighborhood.get(key) for key in parent1[blocks]])
    sub = abs(list_speed[-1] * multi_neighborhood_population - min_speed * multi_neighborhood_population)
    alpha = 0.25
    return random.uniform(abs(parent1[BW] - alpha * sub), parent1[BW] + alpha * sub)


def mutation_blocks(parent1, parent2):  # parent is type list
    rand_p1 = random.randint(0, len(parent1) - 1)
    rand_p2 = random.randint(0, len(parent2) - 1)

    temp1 = parent1[rand_p1]
    temp2 = parent2[rand_p2]
    parent1[rand_p1] = temp2
    parent2[rand_p2] = temp1

    random.shuffle(parent1)

    return parent1, parent2


def mutation_tower(parent1):
    newx, newy = random.uniform(parent1[0] - 1, parent1[0] + 1), random.uniform(parent1[1] - 1, parent1[1] + 1)
    if newx < 0:
        newx = 0
    elif newx > 20:
        newx = 20
    if newy < 0:
        newy = 0
    elif newy > 20:
        newy = 20
    return (newx, newy)


# Define the genetic operators
def mutation(chromosome):
    for gen in chromosome:
        if random.uniform(0, 10) <= mutation_rate * 10:
            rand = random.randint(0, len(chromosome) - 1)
            gen[blocks], chromosome[rand][blocks] = mutation_blocks(gen[blocks], chromosome[rand][blocks])

            gen[location] = mutation_tower(gen[location])

            gen[BW] = mutation_bw(gen)
def chart():
    # Generate x-axis values using range() function
    x = range(len(chart_fitness))

    # Create line plot
    plt.plot(x, chart_fitness)

    # Add labels and title
    plt.xlabel('Index')
    plt.ylabel('fitness')
    plt.title('fitness of chromosome')

    # Show the plot
    plt.show()


def genetic_algorithm(num_of_tows):
    num_of_chromosome = 50
    num_of_generations = 200
    chros = [[create_chromosome(num_of_tows), 0, 1] for i in range(num_of_chromosome)]

    for chromosome in chros:
        chromosome[1] = fitness(chromosome[0])

    sorted(chros, key=itemgetter(1))

    for i in range(num_of_generations):
        new_generation = list()
        # rand = random.sample(range(0, 50), 50)

        # sorted(chros, key=itemgetter(1))
        num_of_crossover = int(crossover_rate * num_of_chromosome)
        if num_of_crossover % 2 == 1:
            num_of_crossover -= 1

        for j in range(int(num_of_crossover / 2)):
            temp1, temp2 = crossover(chros[2 * j][0], chros[2 * j + 1][0])
            new_generation.append(temp1)
            new_generation.append(temp2)

        for newChro in new_generation:
            mutation(newChro)

        for j in range(len(new_generation)):
            new_fit = fitness(new_generation[j])

            for k in range(len(chros)):
                if chros[k][2] > 15 or chros[k][1] < new_fit:
                    chros[k] = [new_generation[j], new_fit, 0]
                    sorted(chros, key=itemgetter(1))
                    break
        
        # chart_fitness.append(chros[0][1])
        chart_fitness.append(chros[0][1])
        for ch in chros:
            ch[2] += 1
    chart()
    chart_fitness.clear()
    best_chromosome = max(chros, key=itemgetter(1))

    return best_chromosome


def find_best_city(lower_city, higher_city):

    totoal_city_list.append(lower_city)
    totoal_city_list.append(higher_city)
    
    len_low = len(lower_city[0])
    len_high = len(higher_city[0])
    if len_high - len_low == 1:
        if lower_city[1] >= higher_city[1]:

            return lower_city

        else:
            return higher_city

    num_of_tows = int((len_low + len_high) / 2)
    current_chromosome = genetic_algorithm(num_of_tows)
    # chart_fitness.append(current_chromosome[1])
    totoal_city_list.append(current_chromosome)

    if lower_city[1] >= higher_city[1]:
        return find_best_city(lower_city, current_chromosome)

    if lower_city[1] < higher_city[1]:
        return find_best_city(current_chromosome, higher_city)


calculate_population()

first_city = genetic_algorithm(10)
second_city = genetic_algorithm(50)

best_city = find_best_city(first_city, second_city)

print(best_city)



