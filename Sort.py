import numpy as np
myMatrix = np. array ([[15.24, 33.68, 73.59],[32.54, 45.68, 63.59],[51.54, 28.39, 9.29]])

print("Original Matrix is :")
print(myMatrix)
print("\nSorting the above array by row in ascending order:")
print(np.sort(myMatrix,axis=1))
print("\n Sorting the above array by column in ascending order:")
print(np.sort(myMatrix,axis=0))