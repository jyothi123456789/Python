import numpy as np
firstArray =np.ones([4,4],dtype=int)
secondArray =np.zeros([4,2],dtype=int)
concatArray = np.concatenate([firstArray,secondArray],axis=1)


print ("The First Array is :",firstArray)
print ("The First Array dimension is : ", firstArray .ndim)
print ("The Second Array is :",secondArray)
print ("The Second Array dimension is : ",secondArray.ndim)
print ("The Concatinated array of first array and second array is :",concatArray)
print ("The Concatinated array of first array and concat array is :",secondArray)
print ("The Concatinated array of second array and concat array is :",firstArray)