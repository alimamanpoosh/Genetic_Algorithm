# import numpy as np

# def COV(x,y):
#     sigma_inverted = [[1/8, 0], [0, 1/8]]

#     X = np.array(x)
#     Y = np.array(y)

#     subtract = np.subtract(X, Y)

#     return np.exp(-0.5*(subtract) * sigma_inverted * np.transpose(subtract))


# Address_tower = (0.5, 1.2971535783035146)
# print(COV(Address_tower[0], Address_tower[1]))


import numpy as np

def COV(x,y):
    sigma_inverted = np.array([[1/8, 0], [0, 1/8]])

    X = np.array(x)
    Y = np.array(y)

    subtract = np.subtract(X, Y)

    return np.exp(-0.5*(subtract) @ sigma_inverted @ np.transpose(subtract))


Address_tower = (0.5, 1.2971535783035146)
Address_tower1 = (2.0, 5.320772063252185)
Address_tower2 = (3.0, 5.732347245259071)


print(COV(Address_tower, Address_tower))
