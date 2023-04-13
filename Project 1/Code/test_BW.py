import numpy as np

def calculate_population():  
    with open('blocks_population.txt') as f:
        lines = f.read().splitlines()

    neighborPopulation = []
    for i in lines:
        neighborPopulation.extend(i.split(','))

    result = np.array(neighborPopulation, dtype=int)
    totalPopulation = np.sum(result)
    dict_neighborhood = {}
    for i in range(400):
        dict_neighborhood[i] = result[i]
    return dict_neighborhood, totalPopulation

def nominal_bandwidth(Bw_ty, bj, blocks):
    dict_neighborhood , totalPopulation = calculate_population()
    # blocks = dict_neighborhood.get(blocks) for key in blocks
    blocks_population = [dict_neighborhood.get(key) for key in blocks]
    bj = dict_neighborhood.get(bj)
    return Bw_ty * bj / sum(blocks)

print(nominal_bandwidth(100, 24, [24, 11, 26, 40, 21]))