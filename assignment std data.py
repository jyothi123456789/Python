# create a text file of student table s.name s.rollno marks age

import os
import pickle
os.chdir("C:\\Users\DELL 5480\PycharmProjects\\new_file\\read_file")
student_dtls = open("C:\\Users\DELL 5480\PycharmProjects\\new_file\\read_file\student.txt","w+")
student_dtls.write("student_name \t s_Rollno \t age \t marks")
mylist = []
while True:

    student_name = input("Enter the student name")
    mylist.read(student_name)
    s_Rollno = int(input("Enter student Rollnum"))
    mylist.read(s_Rollno)
    age = int(input("Enter the student age"))
    mylist.read(age)
    marks = float(input("Enter the marks of student"))
    mylist.read(marks)
    record = input("Enter the new record(y/n):")
    student_dtls.write(str(mylist))
    student_dtls.write("\n")
    if(record== 'y') :
        continue
    else:
        break


