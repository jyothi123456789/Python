# write a program to find negative numbers in a tuple
tuple =(-8,-4,-2,-1,0,1,2,4,8)
for i in tuple:
    if(i < 0):
        print(i)

# concatinate for vowel and store in a list
vowel_list = ['a','e','i','o','u']
vowel = "aeiou"
for i in vowel_list:
    for j in vowel:
        print(i + j)

# create a directory and file in it and print 3 multiples range 51 to 71

for i in range(51, 72):
    if i % 3 == 0:
        print(i, end = ' ')

import os
print(os.getcwd())
os.chdir("C:\\Users\DELL 5480\PycharmProjects")
#os.mkdir("C:\\Users\DELL 5480\PycharmProjects\\new_file")
print("The active directory is:", os.path)
my_file = open("C:\\Users\DELL 5480\PycharmProjects\\new_file\\text.txt","r+")
my_file.seek(0,0)
for i in range(0,101):
    my_file.write(str(i))
    my_file.write("\n")
    print(my_file.read())

for k in my_file:
    for j in range(51, 72):
        if j % 3 == 0:
            print(j, file = my_file)
    my_file.close()
    my_file.write(str(j))
    my_file.write("\n")
    my_file.seek(0,0)
    print(my_file.read())

# write a program in read mode only to read 10th character in the 2nd line
import os
os.chdir("C:\\Users\DELL 5480\PycharmProjects\\new_file")
#os.mkdir("C:\\Users\DELL 5480\PycharmProjects\\new_file\\read_file")
print("the active directory is:", os.path)
task_file = open("C:\\Users\DELL 5480\PycharmProjects\\new_file\\read_file\charerter.txt", "r+")
task_file.write("\n You should not use any of the JavaScript reserved keywords as a variable name.\n These keywords are mentioned in the next section. For example,break or boolean variable names are not valid.")
print(task_file.read())
lines = task_file.readline()
'''
if len(lines) == str(2):
             return lines[9]
else:
    return None
'''
#line1= ("\nThis is python practice session" )
task_file.seek(0,0)
print(task_file.read())
print("The length of task_file is :", len(str(task_file)))
task_file.close()


# create a text file of student table s.name s.rollno marks age

















