# Day 33 - Histograms & Boxplots

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(42)
data = np.random.randint(20, 100, 50)

print("Dataset:", data)

# 1. Histogram
plt.figure()
plt.hist(data, bins=10)

plt.title("Histogram of Data")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()


# 2. Boxplot
plt.figure()
plt.boxplot(data)

plt.title("Boxplot of Data")

plt.show()


# 3. Compare Two Datasets
data2 = np.random.randint(30, 120, 50)

plt.figure()
plt.boxplot([data, data2])

plt.title("Comparison of Two Datasets")

plt.show()
