import os
new_file = open("C:\\Users\\ADMIN\PycharmProjects\pythonProject\\venv\\word.pdf","rb")
print("curent working directory:",os.getcwd())
print("active directory:", os.path.abspath(os.curdir))
output_file = open("C:\\Users\\ADMIN\PycharmProjects\pythonProject\\venv\outputfile.pdf","ab+")
content = new_file.read()
print("Content in word.pdf is : ",content)
#print(os.getcwd())

 