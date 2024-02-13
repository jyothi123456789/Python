import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
mydb=client['Employee']
information=mydb.table2
employeeno=[]

n=int(input("Enter number of Employees : "))

for i in range(n):
    print("-"*50)
    Emp_no=int(input("\nEnter Employee Number : "))
    Emp_Name=input("Enter Employee Name : ")
    Emp_Org=input("Enter Organization Name : ")
    Job_Role=input("Enter Role of Employee : ")
    Hire_Date=input("Enter Joining Date : ")
    dept_no=int(input("Enter Dept No : "))
    Sal=float(input("Enter your Salary : "))
    records=[{
        "Emp NO" : Emp_no,
        "Emp Name" : Emp_Name,
        "Emp_Org" : Emp_Org,
        "Job":Job_Role,
        "Hire Date":Hire_Date,
        "Dept NO":dept_no,
        "Salary" : Sal
    }]
    information.insert_many(records)
print('\n','-'*100)

class Employees:
    def __init__(self, name):
        self.name = name
        self.relationships = []

class Organization:
    def __init__(self, name):
        self.name = name

Employees.name=Emp_Name
Organization.name=Emp_Org

print("Latest entered employee name is : ",Employees.name)
print("Latest entered employee Organization name is : ",Organization.name)
print('-'*100,"\nEntered Details are pushed to MongoDB successfully")
print('-'*100)