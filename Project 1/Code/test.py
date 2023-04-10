import random
import numpy as np
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

print(create_chromosome(3, 5))


