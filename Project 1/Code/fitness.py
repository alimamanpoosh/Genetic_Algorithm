import json
import numpy as np

totalPopulation = 0
dict_neighborhood = {}

location='location'
blocks='blocks'
BW='BW'

def COV(x,y):
    sigma_inverted = np.array([[1/8, 0], [0, 1/8]])

    X = np.array(x)
    Y = np.array(y)

    subtract = np.subtract(X, Y)

    return np.exp(-0.5*(subtract) @ sigma_inverted @ np.transpose(subtract))



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



def nominal_bandwidth(Bw_ty, bj, blocks):
    # dict_neighborhood , totalPopulation = calculate_population()
    # blocks = dict_neighborhood.get(blocks) for key in blocks
    blocks_population = [dict_neighborhood.get(key) for key in blocks]
    bj = dict_neighborhood.get(bj)
    return Bw_ty * bj / sum(blocks)


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

    #return tower_construction_cost, tower_maintanance_cost, user_satisfaction_levels, user_satisfaction_scores


#result = (500, 1, [0.2, 1, 3], [10, 20, 40])
#test = {'tower_construction_cost': 500, 'tower_maintanance_cost': 1, 'user_satisfaction_levels': [0.2, 1, 3],
#        'user_satisfaction_scores': [10, 20, 40]}

#print(fitness())