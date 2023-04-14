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

location='location'
blocks='blocks'
BW='BW'


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
    chromosome=[]
    n=400/NumOfGens
    for i in range(NumOfGens):
        gen=dict()

        x=random.uniform(0,400)
        y=random.uniform(0,400)
        gen[location]=(x,y)

        gen[blocks]=[j for j in range(int(i*(n)),int(n*(i+1)))]

        population=0
        for b in gen[blocks]:
            population+=dict_neighborhood[b]
        gen[BW]=random.uniform(0, 3 * population)

        chromosome.append(gen)

    return chromosome


def nominal_bandwidth(Bw_ty, bj, blocks):
    pop=0
    for b in blocks:
        pop+=dict_neighborhood[b]

    return dict_neighborhood[bj]*Bw_ty/pop


def COV(x,y):
    sigma_inverted = np.array([[1/8, 0], [0, 1/8]])

    X = np.array(x)
    Y = np.array(y)

    subtract = np.subtract(X, Y)

    return np.exp(-0.5*(subtract) @ sigma_inverted @ np.transpose(subtract))


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

    fit=0
    for gen in (chromosome):
        total=0
        for block in gen[blocks]:
            BW_prime=nominal_bandwidth(gen[BW], block, gen[blocks])
            BW_block=COV(gen[location], block)*BW_prime
            BW_user=BW_block/dict_neighborhood[block]

            u_score=0
            for i in range(len(user_satisfaction_levels)):
                if BW_user<user_satisfaction_levels[i]:
                    u_score=user_satisfaction_scores[i]
                    break
                if i==2:
                    u_score=user_satisfaction_scores[3]

            b_score=u_score*dict_neighborhood[block]
            cost=tower_construction_cost+tower_maintanance_cost*gen[BW]

            total+=(b_score-cost)

        fit+=total

    return fit


def crossover_Blocks(parent1, parent2, rate=0.9): # list type
    crossover_point = int(len(parent1)*rate)
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

    """Perform crossover blend on two decimal numbers."""
    d = abs(parent1-parent2)
    if parent2>parent1:
        return random.uniform(parent1-alpha*d,parent2+alpha*d), random.uniform(parent1-alpha*d,parent2+alpha*d)
    return random.uniform(parent2 - alpha * d, parent1 + alpha * d), random.uniform(parent2 - alpha * d, parent1 + alpha * d)


def crossover(chro1, chro2, rate=0.9):
    crossover_point=rate*len(chro1)
    child1, child2 = chro1, chro2
    for g1,g2 in child1[crossover_point:], child2[crossover_point:]:
        rate=0.9
        g1[blocks], g2[blocks] = crossover_tower(g1[blocks], g2[blocks], rate)
        for i in g1[blocks][int(len(g1)*rate):]:
            for gen in child1:
                for b in gen[blocks]:
                    if b==g1[blocks][i]:
                        g1[blocks][i], g2[blocks][i] = g2[blocks][i], g1[blocks][i]

        g1[location], g2[location] = crossover_tower(g1[location], g2[location])
        g1[BW], g2[BW] = crossover_BW(g1[BW], g2[BW])



# Define the genetic operators
def mutation(chromosome, mutation_rate=0.01):
    for i in range(len(chromosome)):
        if np.random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # flip the bit
    return chromosome


def genetic_algorithm(numOfTows):
    numOfChromosome = 50
    numOfGenerations = 200
    chros=[[CreateChromosome(numOfTows), 0, 1] for i in range(numOfChromosome)]

    for chromosome in chros:
        chromosome[1] = fitness(chromosome[0])

    for i in range(numOfGenerations):
        newGeneration=list()
        rand=random.choice(range(0,50), k=50)
        for j in range(int(numOfGenerations/2)):
            temp1, temp2 = crossover(chros[2*j][0], chros[2*j+1][0])
            newGeneration.append(temp1)
            newGeneration.append(temp2)

        for newChro in newGeneration:
            mutation(newChro, 0.1)

        for j in range(len(newGeneration)):
            newFit = fitness(newGeneration[j])

            for k in range(len(chros)):
                if chros[k][2]>50 or chros[k][1]<newFit:
                    chros[k]=[newGeneration[j], newFit, 0]
                    break

        for ch in chros:
            ch[2]+=1

    total_fit=0
    for ch in chros:
        total_fit+=ch[1]

    return chros, total_fit





calculate_population()

big_chro=[random.randint(10,100) for i in range(10)]













# # Implement the evolutionary algorithm
# population_size = 100
# mutation_rate = 0.01
# num_generations = 100
#
# population = [create_chromosome() for i in range(population_size)]
# for generation in range(num_generations):
#     # Evaluate the fitness of the population
#     fitness = [fitness_function(chromosome) for chromosome in population]
#
#     # Select the parents for the next generation
#     parents_indices = np.random.choice(range(population_size), size=2, replace=False, p=fitness / np.sum(fitness))
#     parent1 = population[parents_indices[0]]
#     parent2 = population[parents_indices[1]]
#
#     # Generate the offspring for the next generation
#     offspring1, offspring2 = crossover(parent1, parent2)
#     offspring1 = mutation(offspring1, mutation_rate)
#     offspring2 = mutation(offspring2, mutation_rate)
#
#     # Replace the least fit individuals with the offspring
