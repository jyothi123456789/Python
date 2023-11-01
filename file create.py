import os

os.chdir("C:\\Users\DELL 5480\PycharmProjects\pythonProject1")
#os.mkdir("C:\\Users\DELL 5480\PycharmProjects\pythonProject1\\nikhil1.file")
#print("The active directory is :", os.path)
my_file = open("C:\\Users\DELL 5480\PycharmProjects\pythonProject1\\nikhil1.file\\chandu.txt","w+")
my_file.write("\n 1234567 bala")
my_file.seek(0,0)
print("The list is:", my_file.read())
