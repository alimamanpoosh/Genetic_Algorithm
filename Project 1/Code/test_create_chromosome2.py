import random

result = []

# generate 10 lists with random parameters
for i in range(10):
    # generate first parameter as tuple with a multiple of 0.5 or 1 and random range between 0.5 and 20
    first_param = (random.choice([0.5, 1]) * random.randint(1, 40),)
    
    # generate second parameter as a list of non-repetitive integers between 1 and 400 with random length
    second_param_length = random.randint(1, 400)
    second_param = random.sample(range(1, 401), second_param_length)
    
    # generate third parameter as a decimal number between 0 and 1
    third_param = round(random.uniform(0, 1), 2)
    
    result.append([first_param, second_param, third_param])
    
print(result)

