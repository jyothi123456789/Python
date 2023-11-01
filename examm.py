import os
def calculator():
    pass
print("I am creating new folder in c:Drive")
for itr in range(10,20,2):
    print(itr)
#os.mkdir((("c:\ExceptionHandling")))
os.chdir("c:")
print(os.listdir)

try:
    num1 =100
    num2 = 0
    myDivision= num1/num2
 except zeroDivisionError:
    print("updated num2 to 10")
    num2 =10
    print(num2)



from math import *
class POINT:
    x=0
    y=0
    def __init__(self,point1,point2):
        self.x = point1
        self.y = point2
    def set_location(selfx,y):
        self.x = x
        self.y = y
p = POINT(3,-5)
p.set_location(20.35)
print("The set location method updated x,y to:", p.x ,"and" ,p.y)
print(getattr(p,"y"))





