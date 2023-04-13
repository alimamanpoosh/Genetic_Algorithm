import random

# def crossover_blend_tower(parent1, parent2, alpha=0.25):  # tuple type

#     sub =abs( parent1[0] - parent2[0] )
#     amount_of_change = alpha * sub
#     # offspring1_0 = parent1[0] + amount_of_change
#     # offspring1_1 = parent1[1] - amount_of_change
    
#     # offspring1 = (offspring1_0, offspring1_1)

#     # offspring2_0 = parent2[0] + amount_of_change
#     # offspring2_1 = parent2[1] - amount_of_change

#     if parent2[0] < parent1[0]:
#         parent1[0] -= amount_of_change
#     else:
#         parent1[0] += amount_of_change


#     if parent1[0] < parent2[0] :
#         parent2[0] -= amount_of_change
#     else:
#         parent1[0] += amount_of_change


#     if parent2[1] < parent1[1] :
#         parent1[1] -= amount_of_change
#     else:
#         parent1[1] += amount_of_change

    
#     if parent1[1] < parent2[1] :
#         parent2[1] -= amount_of_change
#     else:
#         parent1[1] += amount_of_change
    

#     offspring1 = (parent1[0], parent1[1])   

#     offspring2 = (parent2[0], parent2[1])

#     return offspring1, offspring2


# p_1 = (3.0, 5.732347245259071)
# p_2 = (0.5, 1.2971535783035146)

# print(crossover_blend_tower(p_1, p_2))




import random

def crossover_blend_tower(parent1, parent2, alpha=0.25):  # tuple type

    parent1 = list(parent1)
    parent2 = list(parent2)
    sub = abs(parent1[0] - parent2[0])
    amount_of_change = alpha * sub
    
    if parent2[0] < parent1[0]:
        parent1[0] -= amount_of_change
    else:
        parent1[0] += amount_of_change

    if parent1[0] < parent2[0]:
        parent2[0] -= amount_of_change
    else:
        parent2[0] += amount_of_change

    if parent2[1] < parent1[1]:
        parent1[1] -= amount_of_change
    else:
        parent1[1] += amount_of_change
   
    if parent1[1] < parent2[1]:
        parent2[1] -= amount_of_change
    else:
        parent2[1] += amount_of_change
        
    offspring1 = (parent1[0], parent1[1])   
    offspring2 = (parent2[0], parent2[1])

    return offspring1, offspring2


p_1 = (3.0, 5.732347245259071)
p_2 = (0.5, 1.2971535783035146)

print(crossover_blend_tower(p_1, p_2))


result = ((2.375, 5.107347245259071), (1.125, 1.9221535783035146))