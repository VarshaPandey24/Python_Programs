#creating a class and showing built-in attributes

class A:
    """
    this is a docstring
    """
    def __init__(self):
        print("this is a method")

# there are 4 built-in attributes


print(A.__dict__)
print(A.__doc__)
print(A.__module__)


