import numpy as np

firstArray = np.array([6, 8])
firstArray = np.arange(1, 50, 5)
onesArray = np.ones((1, 3, 2), dtype=int)
zeroArray = np.zeros((3, 2), dtype=float)
myArray = np.linspace(1, 50, 10)  # start point ,end point, count of numbrs required
randomArray = np.random.random(5)  # randomly create a number
oneslikeArray = np.ones_like((1, 3, 2), dtype=int)  # it gives single dimension

rangeArray = np.arange(1, 30, 5)
print("The range array represents : \n ", rangeArray)
print("The range array size and shape are :", rangeArray.size, "&&", rangeArray.shape)
myshapeArray = np.reshape(rangeArray, (3, 2))
myshapeArray[2, 0] = 2000
print("The reshaped array from 1x6 to 3x2 :\n", myshapeArray)

print("My array is :\n ", firstArray)
print("The ones array is:\n ", onesArray)
print("The ones array dimension is: ", onesArray.ndim)
print("The shape of the ones array is :", onesArray.shape)

print("My first zeroarray :\n", zeroArray)
print("The ones array dimension is: ", zeroArray.ndim)
print("The shape of the ones array is :", zeroArray.shape)

print("The array created with linspace : ", myArray)
print("The created array had elements of size: ", myArray.size)

print("The random generated array : ", randomArray)
print("The dimension of random array is :", randomArray.ndim)

print("The ones like array is : ", oneslikeArray)

onesArray1 = np.ones((2, 2))
onesArray1[1, 1] = 8
onesArray1[0, 1] = 5
newArray = 5 * onesArray1 - 3
# newArray[1,1] = 10
print("The ones array is : ", onesArray1)
print("The ones array dimension is : ", onesArray1.ndim)
print("The changed one array is :", newArray)


