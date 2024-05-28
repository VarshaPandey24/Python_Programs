#to find largest element in the list

L =[10,40,2,6,45,20]
max =L[0]
for i in range(0,len(L)):
    if(L[i]>max):
        max =L[i];
print("the max element is",max)