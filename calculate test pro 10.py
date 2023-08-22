'''
import os


nqclass GoodsGST:
    productName="product Name"
    quantity= "qut"
    price = "price"
    Gstparcentage= "GST Percentage"

    def __int__(self,PName,Qty,price,Gstpc):
        self.productName = PName
        self.quantity = Qty
        self.price = price
        self.Gstparcentage = Gstpc
    def displaydetails(self):
        print("the attributes are : ","\n",self.productName,"\n",self.price,"\n",self.quantity,"\n",self.Gstparcentage)
    def updatevalues(self):
        self.productname = input("enter the name of the product :")
        self.quantity = int(input("enter the Quantity of the product : "))
        self.price = int(input("enter the price of the product : "))
        self.Gstparcentage = float(input("enter the percentage of the gst on the product : "))
    def calculateGST(self,GST):
        self.GST = (self.price * self.Gstparcentage) / 100
        print("the GST is : ",self.GST)
Obj = GoodsGST()
Obj.displaydetails()
Obj.updatevalues()
Obj.calculateGST(3)

'''


while(True):
    productName = input("enter the productName:")
    quantity = int(input("enter the quantity:"))
    price = float(input("enter the price:"))
    nextproduct = input("do you want to enter new record: y/n")
    if(nextproduct == 'y' or nextproduct == 'y'):
        continue

    else:
        break












