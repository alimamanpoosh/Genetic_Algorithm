import json

def fitness():
    
    # read problem_config.json file and save in the dictionary
    with open('problem_config.json') as f:
        data = json.load(f)
    tower_construction_cost = data.get('tower_construction_cost')
    tower_maintanance_cost = data.get('tower_maintanance_cost')
    user_satisfaction_levels = data.get('user_satisfaction_levels')
    user_satisfaction_scores = data.get('user_satisfaction_scores')
    return tower_construction_cost, tower_maintanance_cost, user_satisfaction_levels, user_satisfaction_scores


 
result = (500, 1, [0.2, 1, 3], [10, 20, 40])
test = {'tower_construction_cost': 500, 'tower_maintanance_cost': 1, 'user_satisfaction_levels': [0.2, 1, 3], 'user_satisfaction_scores': [10, 20, 40]}

print(fitness())
