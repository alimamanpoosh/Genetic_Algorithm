import random
import numpy as np

totalPopulation = 0
dict_neighborhood = {}

location='location'
blocks='blocks'
BW='BW'

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

calculate_population()
print(CreateChromosome(20))







[{'location': (80.94341046001658, 89.66392594545339), 'blocks': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 'BW': 3847.563792655824},
 {'location': (359.51168496098984, 271.9331232925899), 'blocks': [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], 'BW': 17340.081704330398},
 {'location': (144.55544994409152, 360.7525925306128), 'blocks': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], 'BW': 10168.945872526592}, {'location': (260.6860893966571, 272.1288757068163), 'blocks': [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], 'BW': 26605.622964388007}, {'location': (238.6267957828178, 233.3883632965203), 'blocks': [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'BW': 20707.41859506214}, {'location': (74.83707154926074, 151.4055529439364), 'blocks': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119], 'BW': 4823.773398560745}, {'location': (61.36626559606286, 148.51998522867765), 'blocks': [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139], 'BW': 9599.773285965446}, {'location': (369.1414273009994, 157.20982355780654), 'blocks': [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159], 'BW': 4565.1950498637025}, {'location': (124.22639689891955, 108.77650803023103), 'blocks': [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179], 'BW': 1847.5100741869217}, {'location': (311.4606291658994, 15.690182301188527), 'blocks': [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199], 'BW': 12308.493644932487}, {'location': (134.2722340591302, 234.36145584880532), 'blocks': [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219], 'BW': 30776.195677788466}, {'location': (14.191935154120605, 55.664876925689114), 'blocks': [220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239], 'BW': 17705.477866879584}, {'location': (49.72341112001119, 380.42399151783843), 'blocks': [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259], 'BW': 2957.888015133766}, {'location': (280.54980801203817, 48.50905060549362), 'blocks': [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279], 'BW': 3825.7442815188274}, {'location': (162.42241451937264, 108.70726998801618), 'blocks': [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299], 'BW': 25668.686353191617}, {'location': (156.30377500287014, 65.69647904831788), 'blocks': [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319], 'BW': 6229.6150625558985}, {'location': (276.13163492209367, 3.260442504473726), 'blocks': [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339], 'BW': 19787.765487617362}, {'location': (83.5058670628261, 155.1242239490671), 'blocks': [340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359], 'BW': 19055.20694153021}, {'location': (378.48014109914703, 370.3593086194665), 'blocks': [360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], 'BW': 27421.752555387822}, {'location': (334.3135802013694, 392.6626147523837), 'blocks': [380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], 'BW': 23616.316751966115}]





















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













