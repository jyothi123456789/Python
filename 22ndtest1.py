class area:
    def area(self):
        print("this calulates the area of the square")
    def area(self,side):
        area = side * side
        print("the area of the square:",area)
    def area(self,length,breadth):
        area = length * breadth
        print("the area of the rectangle is:",area)
a = area()
l = int(input("enter length:"))
b = int(input("enter breadth:"))
a.area(l,b)



