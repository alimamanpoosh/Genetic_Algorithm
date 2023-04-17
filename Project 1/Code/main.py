import numpy as np
import random
import json

# Define the problem parameters
num_neighborhoods = 400
min_speed = 0.2  # megabit
list_speed = [0.2, 1, 3]
max_cost = 10000  # arbitrary cost limit
speed_weights = 0.2
cost_weights = 0.8

totalPopulation = 0
dict_neighborhood = {}

location = 'location'
blocks = 'blocks'
BW = 'BW'


# This function calculates the total population of the neighborhood
def calculate_population():
    with open('blocks_population.txt') as f:
        lines = f.read().splitlines()

    neighborPopulation = []
    for i in lines:
        neighborPopulation.extend(i.split(','))

    result = np.array(neighborPopulation, dtype=int)
    totalPopulation = np.sum(result)
    for i in range(400):
        dict_neighborhood[i] = result[i]


# Define the chromosome representation
def CreateChromosome(NumOfGens):
    chromosome = []
    n = 400 // NumOfGens
    rand = random.sample(range(0,400), 400)
    for i in range(NumOfGens):
        gen = dict()

        x = random.uniform(0, 400)
        y = random.uniform(0, 400)
        gen[location] = (x, y)


        gen[blocks] = [j for j in rand[i*n:n*(i+1)]]

        population = 0
        for b in gen[blocks]:
            population += dict_neighborhood[b]
        gen[BW] = random.uniform(0, 3 * population)

        chromosome.append(gen)

    return chromosome


def nominal_bandwidth(Bw_ty, bj, blocks):
    pop = 0
    for b in blocks:
        pop += dict_neighborhood[b]

    return dict_neighborhood[bj] * Bw_ty / pop


def COV(x, y):
    sigma_inverted = np.array([[1 / 8, 0], [0, 1 / 8]])

    X = np.array(x)
    Y = np.array(y)

    subtract = np.subtract(X, Y)

    return np.exp(-0.5 * (subtract) @ sigma_inverted @ np.transpose(subtract))


# Define the fitness function
def fitness(chromosome):
    # read problem_config.json file and save in the dictionary
    with open('problem_config.json') as f:
        data = json.load(f)
    tower_construction_cost = data.get('tower_construction_cost')
    tower_maintanance_cost = data.get('tower_maintanance_cost')
    user_satisfaction_levels = data.get('user_satisfaction_levels')
    user_satisfaction_scores = data.get('user_satisfaction_scores')
    # tow_blocks, tow_pup = calculate_population()

    fit = 0
    for gen in (chromosome):
        total = 0
        for block in gen[blocks]:
            BW_prime = nominal_bandwidth(gen[BW], block, gen[blocks])
            BW_block = COV(gen[location], block) * BW_prime
            BW_user = BW_block / dict_neighborhood[block]

            u_score = 0
            for i in range(len(user_satisfaction_levels)):
                if BW_user < user_satisfaction_levels[i]:
                    u_score = user_satisfaction_scores[i]
                    break
                if i == 2:
                    u_score = user_satisfaction_scores[3]

            b_score = u_score * dict_neighborhood[block]
            cost = tower_construction_cost + tower_maintanance_cost * gen[BW]

            total += (b_score - cost)

        fit += total

    return fit


def crossover_Blocks(parent1, parent2, rate=0.9):  # list type
    crossover_point = int(len(parent1) * rate)
    offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return offspring1, offspring2


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
    if parent2 > parent1:
        return random.uniform(parent1 - alpha * d, parent2 + alpha * d), random.uniform(parent1 - alpha * d,
                                                                                        parent2 + alpha * d)
    return random.uniform(parent2 - alpha * d, parent1 + alpha * d), random.uniform(parent2 - alpha * d,
                                                                                    parent1 + alpha * d)


def crossover(chro1, chro2, rate=0.9):
    crossover_point = int(rate * len(chro1))
    child1, child2 = chro1, chro2
    for g1, g2 in zip(child1[crossover_point:], child2[crossover_point:]):
        g1[blocks], g2[blocks] = crossover_Blocks(g1[blocks], g2[blocks], rate)
        c = int(len(g1) * rate)
        for i in range(len(g1[blocks][c:])):
            for gen in child1:
                for b in gen[blocks]:
                    if b == g1[blocks][i + c]:
                        g1[blocks][i + c], g2[blocks][i + c] = g2[blocks][i], g1[blocks][i]

        g1[location], g2[location] = crossover_tower(g1[location], g2[location])

        g1[BW], g2[BW] = crossover_BW(g1[BW], g2[BW])

    return child1, child2


def mutation_BW(parent1):  # parent decimal number
    Multi_neighborhood_population = sum([dict_neighborhood.get(key) for key in parent1[blocks]])
    sub = 3 * Multi_neighborhood_population - 0.2 * Multi_neighborhood_population
    alpha = 0.5
    return random.uniform(parent1[BW] - alpha * sub, parent1[BW] + alpha * sub)


def mutation_Blocks(parent1, parent2):  # parent is type list
    rand_P1 = random.randint(0, len(parent1) - 1)
    rand_P2 = random.randint(0, len(parent2) - 1)

    temp = parent1[rand_P1]
    temp2 = parent2[rand_P2]
    parent1[rand_P1] = temp2
    parent2[rand_P2] = temp

    return parent1, parent2


def mutation_tower(parent1):
    newx, newy = random.uniform(parent1[0] - 1, parent1[0] + 1), random.uniform(parent1[1] - 1, parent1[1] + 1)
    if newx < 0:
        newx = 0
    elif newx > 400:
        newx = 400
    if newy < 0:
        newy = 0
    elif newy > 400:
        newy = 400;
    return (newx, newy)


# Define the genetic operators
def mutation(chromosome, mutation_rate=0.1):
    for gen in chromosome:
        if random.randint(1, 10) == 1:
            rand = random.randint(0, len(chromosome) - 1)
            gen[blocks], chromosome[rand][blocks] = mutation_Blocks(gen[blocks], chromosome[rand][blocks])

            gen[location] = mutation_tower(gen[location])

            gen[BW] = mutation_BW(gen)


def genetic_algorithm(numOfTows):
    numOfChromosome = 50
    numOfGenerations = 200
    chros = [[CreateChromosome(numOfTows), 0, 1] for i in range(numOfChromosome)]

    for chromosome in chros:
        chromosome[1] = fitness(chromosome[0])

    for i in range(numOfGenerations):
        newGeneration = list()
        rand = random.sample(range(0, 50), 50)
        for j in range(25):
            temp1, temp2 = crossover(chros[rand[2 * j]][0], chros[rand[2 * j + 1]][0])
            newGeneration.append(temp1)
            newGeneration.append(temp2)

        for newChro in newGeneration:
            mutation(newChro, 0.1)

        for j in range(len(newGeneration)):
            newFit = fitness(newGeneration[j])

            for k in range(len(chros)):
                if chros[k][2] > 50 or chros[k][1] < newFit:
                    chros[k] = [newGeneration[j], newFit, 0]
                    break

        for ch in chros:
            ch[2] += 1

    total_fit = 0
    for ch in chros:
        total_fit += ch[1]

    return chros, total_fit


def find_best_city(lower_city, higher_city):
    len_low = len(lower_city[0][0])
    len_high = len(higher_city[0][0])
    if len_high - len_low == 1:
        if lower_city[1] >= higher_city[1]:
            return lower_city
        else:
            return higher_city

    numOfTows = (len_low + len_high) // 2
    current_chros, current_fitness = genetic_algorithm(numOfTows)

    if lower_city[1] > higher_city[1]:
        return find_best_city(lower_city, (current_chros, current_fitness))

    if lower_city[1] <= higher_city[1]:
        return find_best_city((current_chros, current_fitness), higher_city)


calculate_population()

first_city = genetic_algorithm(10)
second_city = genetic_algorithm(50)

best_city = find_best_city(first_city, second_city)

print(best_city)
