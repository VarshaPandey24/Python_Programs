
try :
    file =open('B.txt','r')
    print("is file closed ",file.closed)
    file.close()
    print("is now the file is closed",file.closed)

except FileNotFoundError as e:
    print('file is not found at the specified location')

except IOError as e:
    print("some error occured whike reading the file")

