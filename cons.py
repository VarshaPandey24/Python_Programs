#constructor overloading

class A:
    def __init__(self,arg1="good",arg2="Hello"):
        
        if arg1 is not None and arg2 is not None:
            self.arg1 =arg1
            self.arg2 =arg2
        elif arg1 is not None:
            self.arg1 =arg1
            self.arg2 ="default value"
        else:
            arg1="default value"
            arg2 ="default value"
    def display(self):
        print("arg1: ",self.arg1,"arg2: ",self.arg2)

obj1=A()
obj2 =A("one attribute")
obj3 =A("both1","both2")

obj1.display()
obj2.display()
obj3.display()



            