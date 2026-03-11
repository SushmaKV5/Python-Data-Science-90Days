import numpy as np
import time

size = 1000000
print("\n===Creating Data===")

#Creating the lists
list1 = list(range(size))
list2 = list(range(size))

#Creating NumPy arrays
array1 = np.array(list1)
array2 = np.array(list2)

#Python list addition
print("===Python Lists addition===")
start = time.time()

result_list = []
for i in range(size):
  result_list.append(list1[i] + list2[i])

end = time.time()
print("Python list computation", end-start, "seconds")

#NumPy array addition
print("\n===NumPy Array Addition===")
start = time.time()

result_array = array1 + array2

end = time.time()
print("NumPy array computation", end-start, "seconds")

#Show small result sample
print("\nSample output:\n")
print("List result(first 5):", result_list[:5])
print("NumPy array result(first 5):", result_array[:5])
