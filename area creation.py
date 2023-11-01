class area:
    def area():

        print("The area of the square is :",area)
    def area(self ,l1):
         area = l1 * l1
         print("The area of the square is :",area)

    def area(self, l1,b1):
        area = l1 * b1
        print("The area of rectangle is : ",area)
a = area()
l1 = int(input("Enter the Length : "))
b1 = int(input("Enter the breadth : "))
a.area(l1,b1)
