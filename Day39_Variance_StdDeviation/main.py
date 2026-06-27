import numpy as np
import pandas as pd

# Sample dataset
data = [10, 20, 20, 30, 40, 50, 60, 60, 60, 70]

print("Dataset:", data)

# Convert to NumPy array
arr = np.array(data)

# Variance
variance = np.var(arr)
print("\nVariance:", variance)

# Standard Deviation
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)

# Using Pandas
series = pd.Series(data)

print("\nUsing Pandas:")
print("Variance:", series.var())
print("Standard Deviation:", series.std())
