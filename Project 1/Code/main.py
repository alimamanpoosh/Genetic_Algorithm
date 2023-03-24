import numpy as np


def calculate_population(): # This function calculates the total population of the neighborhood
    with open('blocks_population.txt') as f:
        lines = f.read().splitlines()

    neighborPopulation = []
    for i in lines:
        neighborPopulation.extend(i.split(','))

    result = np.array(neighborPopulation, dtype=int)
    totalPopulation = np.sum(result)
    return totalPopulation

