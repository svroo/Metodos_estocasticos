import numpy as np
from numpy import random

def generate_cumulative_probabilities(probabilities):
    cumulative_probabilities = [0] * len(probabilities)
    for i, prob in enumerate(probabilities):
        cumulative_probabilities[i] = cumulative_probabilities[i-1] + prob
    return cumulative_probabilities

def get_value(u, values, cumulative_probabilities):
    for i, prob in enumerate(cumulative_probabilities):
        if u < prob:
            return values[i]

probabilities = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
values = [1, 2, 3, 4, 5, 6]
cumulative_probabilities = generate_cumulative_probabilities(probabilities)

results = []
for i in range(10):
    u = random.random()
    results.append(get_value(u, values, cumulative_probabilities))

print(results)