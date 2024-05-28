#to read a file line by line and write it into a list in another file

file =open("A.txt",'r')
contents =file.readlines()
print(type(contents))
print(contents)

file2 =open("B.txt",'a+')

file2.writelines(contents)

data =file2.read()
print(data)
