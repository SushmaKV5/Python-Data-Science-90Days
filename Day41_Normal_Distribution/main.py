import numpy as np
import matplotlib.pyplot as plt

# Generate normally distributed data
mean = 50
std_dev = 10

data = np.random.normal(mean, std_dev, 1000)

print("Sample Data:", data[:10])

# Plot Histogram
plt.figure()
plt.hist(data, bins=30)

plt.title("Normal Distribution (Mean=50, Std=10)")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()


# Compare different distributions
data1 = np.random.normal(50, 10, 1000)
data2 = np.random.normal(60, 5, 1000)

plt.figure()
plt.hist(data1, bins=30, alpha=0.5)
plt.hist(data2, bins=30, alpha=0.5)

plt.title("Comparison of Two Normal Distributions")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
