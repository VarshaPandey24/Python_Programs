#to remove empty tuples from list

L =[(1,2),(),(4,3,2),(1,7),()]

for i in range(0,len(L)):
    a =L[i]
    b =len(a)
    if (b==0):
        del L[i]
    else:
        pass    
print(L)    