#program for fibonacci series

def fibo(n):
    num1 =0
    num2=1
    nextnum =num2;
    print(num1)
    print(num2)
    i=0;
    while(i<n):
        print(nextnum)
        num1,num2 =num2,nextnum
        nextnum =num1+num2
        i+=1

n =int(input("enter the number for calculating fibonacci"))
fibo(n)