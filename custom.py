#this is a program for showing custom exception

#first we create a custom exception class

class ShortTextError(Exception):
    def __init__(self,message="text length is less than 3 characters"):
        self.message =message
    #function for checking length and raising
def check(text):
    if len(text)<3:
        raise ShortTextError()
    else:
        print("you entered this text:",text)
#main code

try:
    text ="125678"
    check(text)

except ShortTextError as e:
    print("Custom Error:",e.message)



