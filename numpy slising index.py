import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing elements and slices
print("Element at (1,2):", arr[1, 2])
print("First column:", arr[:, 0])
print("Subarray:")
print(arr[1:, 1:])
