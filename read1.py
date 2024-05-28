#to read entire text file
try:
    fileh =open("A.txt",'r')
    contents=fileh.read()
    print(contents)

    fileh.close()
    print(fileh.closed)

except FileNotFoundError as e:
    print("file not found at specified location")    

    