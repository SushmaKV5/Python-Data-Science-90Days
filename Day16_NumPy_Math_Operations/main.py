import numpy as np

# 1. Creating NumPy Arrays
print("=== Creating Arrays ===")
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("Array 1:", arr1)
print("Array 2:", arr2)

# 2. Basic Mathematical Operations (Element-wise)
print("\n=== Element-wise Operations ===")
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# 3. Scalar Operations
print("\n=== Scalar Operations ===")
print("Array + 5:", arr1 + 5)
print("Array * 2:", arr1 * 2)

# 4. Aggregate Functions
print("\n=== Aggregate Functions ===")
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))

# 5. Square and Square Root
print("\n=== Power Operations ===")
print("Square:", np.square(arr1))
print("Square Root:", np.sqrt(arr1))

# 6. 2D Array Operations
print("\n=== 2D Array Operations ===")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matrix:\n", matrix)
print("Row-wise Sum:", np.sum(matrix, axis=1))
print("Column-wise Sum:", np.sum(matrix, axis=0))
print("Mean of Matrix:", np.mean(matrix))

# 7. Trigonometric Functions
print("\n=== Trigonometric Functions ===")
angles = np.array([0, np.pi/2, np.pi])
print("Sin values:", np.sin(angles))
print("Cos values:", np.cos(angles))