list1=[1,2,3,4]
list2=[6,7,8,9]
print("the list 1 is :", list1)
print("the length of list 1 is :",len(list1))
print("the type of list 1 is :",type(list1))
print(" the memory for list is:",id(list1))

print("the list 2 is:",list2)
print("the length of list 2 is:",len(list2))
print("the type of list 2 is :",type(list2))
print("the memory of list 2 is :",id(list2))
list1 = list2
print("the list 1 after shallow copy :",list1)
print("the list 2 after shallow copy :",list2)
