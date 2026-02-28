import numpy as np

print("=== Creating Matrices ===")
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# 1. Matrix Addition
print("\n=== Matrix Addition ===")
print("A + B:\n", A + B)

# 2. Matrix Subtraction
print("\n=== Matrix Subtraction ===")
print("A - B:\n", A - B)

# 3. Matrix Multiplication
print("\n=== Matrix Multiplication ===")
print("A * B (element-wise):\n", A * B)
print("A dot B (matrix multiplication):\n", np.dot(A, B))

# 4. Transpose
print("\n=== Transpose ===")
print("Transpose of A:\n", A.T)

# 5. Determinant
print("\n=== Determinant ===")
print("Determinant of A:", np.linalg.det(A))

# 6. Inverse
print("\n=== Inverse ===")
print("Inverse of A:\n", np.linalg.inv(A))

# 7. Identity Matrix
print("\n=== Identity Matrix ===")
I = np.eye(2)
print("Identity Matrix:\n", I)

# 8. Matrix Rank
print("\n=== Matrix Rank ===")
print("Rank of A:", np.linalg.matrix_rank(A))
