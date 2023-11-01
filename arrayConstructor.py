import  numpy as np
firstArray = np.ones([4,4],dtype=int)
secondArray = np.zeros([4,2],dtype=int)
concatArray = np.concatenate([firstArray,secondArray],axis=1)


print("The first array is :", firstArray)





identityMatrix = np.eye(3, dtype=int)
print("The identity matrix is : \n",identityMatrix)





