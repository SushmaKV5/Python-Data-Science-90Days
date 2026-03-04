#Random data generation using NumPy

import numpy as np

print("===Random Integer Generation===")
rand_int = np.random.randint(1,100, size = 10)
print("Random integer:", rand_int)

print("\n===Random Floats Generation (0-1)===")
rand_float = np.random.rand(5)
print("Random floats:", rand_float)

print("\n===Random 2D array===")
rand_matrix = np.random.randint(1, 50, size = (3,3))
print("Random matrix:", rand_matrix)

print("\n=== Normal Distribution ===")
normal_dist = np.random.randn(5)
print("Normal Distribution Values:", normal_dist)

print("\n=== Random Choice ===")
choices = np.random.choice([10, 20, 30, 40], size=5)
print("Random Choices:", choices)

print("\n=== Shuffle Array ===")
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("Shuffled Array:", arr)

print("\n=== Setting Random Seed ===")
np.random.seed(42)
print("Seeded Random Numbers:", np.random.randint(1, 100, 5))
