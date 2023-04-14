import random
#import numpy as np


def CreateChromosome(NumOfGens):
    chromosome=[]
    n=400/NumOfGens
    for i in range(NumOfGens):
        gen=dict()
        location='location'
        blocks='blocks'
        BW='BW'

        x=random.uniform(0,400)
        y=random.uniform(0,400)
        gen[location]=(x,y)

        gen[blocks]=[j for j in range(i*n,n*(i+1))]

        population=0
        for b in gen[blocks]:
            population+=dict_neighborhood[b]
        gen[BW]=random.uniform(0, 3 * population)

        chromosome.append(gen)

    return chromosome































# def create_chromosome(num_lists):
#     param1_range = range(0, 400)  # address each tower
#     param2_range = range(1, 400)  # The number of each neighborhood
#     param3_range = range(1, 6)  # bandwidth each tower  #  min_BW = 0.2 * 191932.0 = 38386.4 Max_BW = 3 * 191932.0 = 57589.6

#     # num_lists = 5 # Define the number of internal lists you want to create
#     chromosome = []
#     for i in range(num_lists):
#         internal_list = [random.choice(param1_range),
#                          random.choice(param2_range),
#                          random.choice(param3_range)]
#         chromosome.append(internal_list)
#     return chromosome

# print(create_chromosome(5))

#
# result_list = []
# for i in range(2):
#     # Generate first parameter: tuple of integer and float multiple of 0.5, between 0.5 and 20
#     int_param = random.uniform(1, 10) * 0.5
#     float_param = random.uniform(0, 12.5) * 0.5 + 0.5
#     first_param = (int_param, float_param)
#
#     # Generate second parameter: list of integers, between 1 and 400, with random length
#     second_param_len = random.randint(1, 50)
#     second_param = [random.randint(1, 50) for _ in range(5)]
#
#     # Generate third parameter: decimal number, randomly selected from a list of possible values
#     third_param_choices = [0.1, 0.2, 0.5, 1.0]
#     third_param = random.choice(third_param_choices)
#     and_num = random.uniform(10, 200)
#
#     # Append sublist to result list
#     result_list.append([first_param, second_param, and_num])
#
# # Print result list
# print(result_list)
#
# [[(3.0, 5.732347245259071), [34, 8, 4, 49, 5], 71.84009214923466]]
# [[(0.5, 1.2971535783035146), [24, 11, 26, 40, 21], 112.95306689655742]]
# [[(2.0, 5.320772063252185), [26, 25, 42, 7, 7], 75.24420678819384]]

# [[(0.5, 1.1673131492280229), [33, 7, 15, 6, 32], 122.80079336052043],
#  [(0.5, 3.770175490060924), [48, 38, 13, 21, 20], 189.23479157228573]]













