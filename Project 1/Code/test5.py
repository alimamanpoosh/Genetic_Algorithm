import random

def crossover_blend_BW(parent1, parent2, alpha=0.25):  # we use avg replace that
    """Perform crossover blend on two decimal numbers."""
    # Determine the blending point
    blend_point = random.uniform(0, 1)
    # Blend the parent values to create the offspring value
    offspring = alpha * parent1 + (1 - alpha) * parent2
    # Apply the blending factor to the offspring value
    offspring = (1 - blend_point) * parent1 + blend_point * offspring 
    return offspring

p_1 = 71.84009214923466
p_2 = 112.95306689655742

print(crossover_blend_BW(p_1, p_2))

result = 88.78595913717476
