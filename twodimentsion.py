import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("the array is:\n",array)
identitymatrix = np.eye(3,dtype=int)
print("the identity matrix is:\n",identitymatrix)
add = array + identitymatrix
print("the addition of the resulted array:\n",add)
multiplication = array * identitymatrix
print("the multiplication of the resulted array:\n",multiplication)

