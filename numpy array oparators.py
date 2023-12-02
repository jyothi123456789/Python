import numpy as np

# Create NumPy arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Perform array operations
result = arr1 + arr2
print("Array Addition:")
print(result)

result = np.dot(arr1, arr2)
print("\nMatrix Multiplication:")
print(result)
