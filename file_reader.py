import file_info
file = open("C:\\Users\DELL 5480\\Desktop\wordsfile\\readfile.pdf", 'rb')
file.seek(0,0)
content = file.read()
print(content)
