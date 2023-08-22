import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("the array is:\n",array)
array1 = np.ones((3,3),dtype=int)
print("the ones array is:",array1)

add = array + array1
print("the addition of the resulted array:",add)
multiplication = array * array1
print("the multiplication of the resulted array:",multiplication)
