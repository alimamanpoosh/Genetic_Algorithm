import random
import numpy as np
import copy

location = 'location'
blocks = 'blocks'
BW = 'BW'


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


def mutation_blocks(parent1, parent2):  # parent is type list
    rand_p1 = random.randint(0, len(parent1) - 1)
    rand_p2 = random.randint(0, len(parent2) - 1)

    parent1[rand_p1], parent2[rand_p2] = parent2[rand_p2], parent1[rand_p1]

    random.shuffle(parent1)

    return parent1, parent2


def crossover(chro1, chro2):
    child1, child2 = copy.deepcopy(chro1), copy.deepcopy(chro2)
    for i in range(len(child1)):
        child1[i][blocks], child2[i][blocks] = crossover_blocks(child1[i][blocks], child2[i][blocks])

        for j in range(len(child1[i][blocks])):
            for gen1, gen2 in zip(child1, child2):
                if gen1 is not child1[i]:
                    if child1[i][blocks][j] in gen1[blocks]:
                        k = gen1[blocks].index(child1[i][blocks][j])
                        gen1[blocks][k] = child2[i][blocks][j]
                elif gen1[blocks].count(child1[i][blocks][j]) > 1:
                    k = gen1[blocks].index(child1[i][blocks][j])
                    gen1[blocks][k] = child2[i][blocks][j]

                if gen2 is not child2[i]:
                    if child2[i][blocks][j] in gen2[blocks]:
                        k = gen2[blocks].index(child2[i][blocks][j])
                        gen2[blocks][k] = child1[i][blocks][j]
                elif gen2[blocks].count(child2[i][blocks][j]) > 1:
                    k = gen2[blocks].index(child2[i][blocks][j])
                    gen2[blocks][k] = child1[i][blocks][j]

        # child1[i][location], child2[i][location] = crossover_tower(child1[i][location], child2[i][location])

        # child1[i][BW], child2[i][BW] = crossover_bw(child1[i][BW], child2[i][BW], len(child1[i][blocks]))

    return child1, child2


def mutation(chromosome):
    for gen in chromosome:
        if random.uniform(0, 10) <= 0.1 * 10:
            rand = random.randint(0, len(chromosome) - 1)
            gen[blocks], chromosome[rand][blocks] = mutation_blocks(gen[blocks], chromosome[rand][blocks])

            # gen[location] = mutation_tower(gen[location])

            # gen[BW] = mutation_bw(gen)

    return chromosome


test = [{'blocks': [25, 64, 287, 256, 167, 361, 375, 49, 283, 174, 238, 62, 42, 162, 347, 161, 69, 120, 151, 153, 247, 321, 251, 327, 277, 316, 181, 208, 345, 395, 98, 334, 220, 145, 65, 21, 328, 323, 215, 275, 144, 73, 109, 195, 355], 'location': (9.404521633282739, 7.266803293592835), 'BW': 89.42619242429137}, {'blocks': [115, 197, 381, 129, 27, 311, 155, 372, 134, 270, 32, 177, 164, 332, 254, 37, 190, 2, 280, 308, 394, 333, 370, 35, 104, 165, 339, 51, 337, 114, 95, 379, 294, 367, 200, 390, 274, 245, 286, 318, 58, 371, 79, 204, 68], 'location': (15.070667532945098, 8.580530025519398), 'BW': 86.51098376168243}, {'blocks': [404, 93, 86, 306, 341, 240, 239, 138, 385, 179, 66, 74, 203, 168, 182, 402, 194, 284, 128, 210, 324, 356, 353, 152, 41, 103, 295, 130, 126, 216, 122, 268, 82, 81, 377, 360, 343, 118, 336, 75, 191, 229, 55, 209, 253], 'location': (10.655540081424554, 9.66261829403568), 'BW': 114.60312706378448}, {'blocks': [232, 143, 50, 236, 392, 249, 227, 246, 296, 53, 330, 140, 387, 205, 26, 257, 264, 285, 10, 276, 278, 313, 113, 184, 258, 326, 217, 4, 399, 352, 292, 67, 17, 383, 137, 36, 199, 279, 262, 72, 8, 187, 357, 148, 389], 'location': (8.088459250645997, 8.545887786753594), 'BW': 96.01314792218888}, {'blocks': [45, 169, 5, 160, 106, 12, 70, 289, 291, 201, 272, 139, 170, 87, 158, 159, 221, 366, 94, 386, 91, 335, 391, 48, 310, 20, 59, 354, 378, 317, 224, 185, 19, 61, 107, 382, 398, 243, 100, 252, 307, 363, 157, 288, 225], 'location': (13.529333467874455, 10.956447525268548), 'BW': 85.04023209497758}, {'blocks': [108, 34, 173, 46, 315, 57, 97, 47, 172, 297, 331, 117, 282, 259, 7, 401, 15, 349, 393, 250, 329, 248, 28, 230, 350, 305, 214, 92, 388, 183, 234, 304, 171, 212, 348, 303, 127, 78, 146, 88, 111, 43, 3, 110, 223], 'location': (11.385632079388465, 10.872103749889021), 'BW': 85.9538715070551}, {'blocks': [218, 219, 23, 163, 260, 44, 342, 1, 56, 22, 242, 237, 90, 312, 149, 320, 16, 14, 400, 244, 271, 154, 96, 101, 376, 340, 314, 6, 384, 71, 150, 131, 33, 136, 290, 374, 188, 83, 233, 112, 80, 116, 397, 89, 365], 'location': (9.785510528851763, 10.482142768339624), 'BW': 176.83028791697222}, {'blocks': [364, 380, 322, 235, 202, 403, 266, 9, 119, 176, 281, 300, 175, 269, 123, 166, 211, 344, 273, 351, 207, 60, 85, 325, 228, 362, 0, 231, 206, 373, 241, 261, 99, 196, 198, 226, 31, 141, 186, 263, 105, 299, 40, 121, 222], 'location': (7.093858918341187, 12.296781581679344), 'BW': 150.39233771765146}, {'blocks': [298, 39, 265, 125, 293, 192, 76, 124, 135, 346, 396, 319, 38, 133, 255, 29, 102, 368, 132, 189, 193, 54, 302, 84, 369, 309, 338, 147, 63, 178, 180, 301, 358, 213, 359, 77, 24, 52, 18, 142, 13, 30, 11, 156, 267], 'location': (11.263372522212773, 9.765909577001903), 'BW': 90.95940848327471}]

ch1 = [{'blocks': [107, 70, 87, 14, 244, 59, 155, 376, 27, 377, 12, 302, 333, 374, 318, 218, 29, 230, 335, 254, 298,
                   203, 45, 300, 382, 201, 273, 104, 166, 13, 16, 320, 271, 95, 386, 317, 149, 216, 215, 388],
        'location': (10.13003049491613, 15.631612823367844), 'BW': 39748.27160566058}, {
           'blocks': [362, 164, 198, 172, 343, 175, 210, 299, 109, 105, 390, 309, 391, 191, 206, 265, 220, 253, 169, 88,
                      262, 78, 18, 129, 152, 229, 267, 357, 291, 231, 145, 0, 251, 77, 173, 65, 315, 222, 348, 6],
           'location': (19.552805130312688, 19.571898514764907), 'BW': 19040.951944290755}]

ch2 = [{'blocks': [6, 193, 234, 188, 60, 362, 161, 391, 34, 375, 370, 353, 19, 83, 334, 155, 64, 172, 307, 228, 13, 263,
                   207, 269, 196, 225, 367, 245, 23, 371, 343, 197, 53, 156, 129, 205, 74, 145, 48, 82],
        'location': (6.938379640536869, 13.487441974859342), 'BW': 14067.747052303372}, {
           'blocks': [345, 7, 184, 357, 340, 287, 201, 382, 342, 202, 106, 73, 147, 256, 363, 282, 292, 3, 286, 336,
                      141, 192, 2, 148, 200, 160, 178, 137, 100, 248, 299, 103, 109, 349, 235, 293, 179, 288, 329, 107],
           'location': (6.603185867549432, 2.66443617890409), 'BW': 46007.12431067439}]

# for i in range(len(test)):
#     test[i]['blocks'].sort()
#     print(i, test[i]['blocks'])
#temp1, temp2 = ch1, ch2
# for j in range(10000):
#     temp1, temp2 = crossover(ch1, ch2)
#     #new_generation.append(temp1)
#     #new_generation.append(temp2)
#
#     # for newChro in new_generation:
#     temp1 = mutation(temp1)
#     temp2 = mutation(temp2)
#
#     ch1, ch2 = temp1, temp2
#     # for j in range(len(new_generation)):
#     #     new_fit = fitness(new_generation[j])
#     #
#     #     for k in range(len(chros)):
#     #         if chros[k][2] > 20 or chros[k][1] < new_fit:
#     #             chros[k] = [new_generation[j], new_fit, 0]
#     #             chros.sort(key=lambda x: x[1])
#     #             break
#
# for i in range(len(temp1)):
#     temp1[i]['blocks'].sort()
#     print(1, i, temp1[i]['blocks'])
# print('\n')
# for i in range(len(temp2)):
#     temp2[i]['blocks'].sort()
#     print(1, i, temp2[i]['blocks'])
#
# print([x for x in temp2[0][blocks] if x in temp2[1][blocks]])

# for j in range(len(temp1)):
#     for i in temp1[j]['blocks']:
#         for k in range(len(temp1)):
#             if i in temp1[k][blocks]:
#                 print(k, i)
#
# for i in range(1000):
#     test[0]['blocks'], test[1]['blocks'] = crossover_blocks(test[0]['blocks'], test[1]['blocks'])
#     test[0]['blocks'], test[1]['blocks'] = mutation_blocks(test[0]['blocks'], test[1]['blocks'])

for i in range(len(test)):
    test[i]['blocks'].sort()
    print(i, test[i]['blocks'])

for i in test[0]['blocks']:
    if i in test[1]['blocks']:
        print(i)
l=list()
for i in range(len(test)):
    l+=test[i][blocks]

l.sort()

print(l, len(l)-len(set(l)))