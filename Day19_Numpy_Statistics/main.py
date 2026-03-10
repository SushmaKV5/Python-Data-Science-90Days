import numpy as np

print("=== Creating Dataset ===")
data = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("Data:", data)

# Mean
print("\n=== Mean ===")
print("Mean:", np.mean(data))

# Median
print("\n=== Median ===")
print("Median:", np.median(data))

# Standard Deviation
print("\n=== Standard Deviation ===")
print("Standard Deviation:", np.std(data))

# Variance
print("\n=== Variance ===")
print("Variance:", np.var(data))

# Minimum and Maximum
print("\n=== Min & Max ===")
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

# Percentiles
print("\n=== Percentiles ===")
print("25th Percentile:", np.percentile(data, 25))
print("50th Percentile:", np.percentile(data, 50))
print("75th Percentile:", np.percentile(data, 75))

# 2D Array Statistics
print("\n=== 2D Data Statistics ===")
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("Matrix:\n", matrix)

print("\nRow-wise Mean:", np.mean(matrix, axis=1))
print("Column-wise Mean:", np.mean(matrix, axis=0))

print("Row-wise Sum:", np.sum(matrix, axis=1))
print("Column-wise Sum:", np.sum(matrix, axis=0))
