import numpy as np
import pandas as pd

# Sample dataset
data = [10, 20, 20, 30, 40, 50, 60, 60, 60, 70]

print("Dataset:", data)

# Convert to NumPy array
arr = np.array(data)

# Mean
mean = np.mean(arr)
print("\nMean:", mean)

# Median
median = np.median(arr)
print("Median:", median)

# Mode (using Pandas)
series = pd.Series(data)
mode = series.mode()

print("Mode:", list(mode))
