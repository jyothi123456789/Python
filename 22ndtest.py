import numpy as np
myarrar = np.array([[1,3,4,5],[1,2,6,7],[3,5,9,8]])
print("the elements in the array is:\n",myarrar)

unique_values ,counts =np.unique(myarrar,return_counts=True)
unique_valu_list=unique_values[counts==1]
print("The distinct values are :",unique_valu_list)