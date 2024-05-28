# ZeroDivisionError
def divide(a,b):
    try:
        result = a/b
        print (result)

    except ZeroDivisionError as e:
        print(" Error:Division By Zero")

divide(1,4)
divide(5,0)

    
