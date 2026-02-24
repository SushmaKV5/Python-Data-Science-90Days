import numpy as np

#Creationg NumPy arrays
print("\nCreating numpy arrays:")
arr1 = np.array([10,20,30,40])
print("1D array:", arr1)

arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print("\n2D array:\n", arr2)

#Array shape and dimensions
print("\n2D array shape:", arr2.shape)
print("Number of dimensions:", arr2.ndim)

#Indexing in 1D array
print("\n=== Indexing (1D) ===")
print("First element:", arr1[0])
print("Last element:", arr1[-1])

#Indexing in 2D Array
print("\n=== Indexing (2D) ===")
print("Element at row 1, col 2:", arr2[1, 2])  # 6
print("Element at row 0, col 1:", arr2[0, 1])  # 2

#Slicing Arrays
print("\n=== Slicing ===")
print("First three elements:", arr1[0:3])
print("Last two elements:", arr1[-2:])

#Row and Column Access
print("\n=== Row & Column Access ===")
print("First row:", arr2[0])
print("Second column:", arr2[:, 1])

#Array Operations
print("\n=== Basic Operations ===")
print("Array + 10:", arr1 + 10)
print("Array * 2:", arr1 * 2)

#Reshaping Array
print("\n=== Reshaping ===")
reshaped = arr1.reshape(5, 1)
print("Reshaped Array:\n", reshaped)
