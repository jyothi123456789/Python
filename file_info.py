import os

my_file = open("C:\\Users\DELL 5480\\Desktop\wordsfile\\readfile.pdf", "rb")
print(os.getcwd())
output_file = open("C:\\Users\DELL 5480\\Desktop\wordsfile\\outputfile.pdf", "ab+")

my_file.close()
