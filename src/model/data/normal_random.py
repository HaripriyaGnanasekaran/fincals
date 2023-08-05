import numpy as np

mean = 0.35
std = 0.39

# generate 10 random numbers from a normal distribution with the given mean and std
random_numbers = np.random.normal(mean, std, 30)

print(random_numbers.mean())
