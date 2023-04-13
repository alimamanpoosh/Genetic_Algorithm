
# crossover function for  nighberhood






import random
import numpy as np

# def saga(parent1, parent2, alpha):
#     """
#     Simple Arithmetic Genetic Algorithm (SAGA) operator for genetic algorithms
#     Inputs:
#     - parent1: a decimal number representing the first parent solution
#     - parent2: a decimal number representing the second parent solution
#     - alpha: a scalar value between 0 and 1 representing the mixing ratio
#     Outputs:
#     - child1, child2: two decimal numbers representing the offspring solutions
#     """
#     child1 = alpha*parent1 + (1-alpha)*parent2
#     child2 = (1-alpha)*parent1 + alpha*parent2
#     return child1, child2


def saga(parent1, parent2):
    """
    Simple Arithmetic Genetic Algorithm (SAGA) operator for genetic algorithms
    Inputs:
    - parent1: a list representing the first parent solution
    - parent2: a list representing the second parent solution
    Outputs:
    - child1, child2: two lists representing the offspring solutions
    """
    # Get the length of the parents
    n = len(parent1)

    # Choose a random splitting point
    split_point = random.randint(0, n-1)

    # Create the offspring solutions
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]

    return child1, child2



def wac(parent1, parent2, alpha):
    """
    Whole Arithmetic Crossover (WAC) operator for genetic algorithms
    Inputs:
    - parent1: a list of numbers representing the first parent solution
    - parent2: a list of numbers representing the second parent solution
    - alpha: a scalar value between 0 and 1 representing the mixing ratio
    Outputs:
    - child: a list of numbers representing the offspring solution
    """
    assert len(parent1) == len(parent2), "Parents must have the same length"
    n = len(parent1)
    child = [0]*n
    for i in range(n):
        child[i] = alpha*parent1[i] + (1-alpha)*parent2[i]
    return child

p1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
p2 = [0.3, 0.2, 0.3, 0.2, 0.3, 0.2, 0.3, 0.2, 0.3]
# print(wac(p1, p2, 0.5))
# print(saga(p1, p2, 0.5))


def crossover(parent1, parent2): #genrate offspring from parent
    crossover_point = np.random.randint(len(parent1))
    offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return offspring1, offspring2




P_1 = [34, 8, 4, 49, 5]
P_2 = [24, 11, 26, 40, 21]
print(saga(P_1, P_2))

result_1 = ([34, 8, 4, 40, 21], [24, 11, 26, 49, 5])

print(crossover(P_1, P_2))
