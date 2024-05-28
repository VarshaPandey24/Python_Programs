#creating a list
L =[1,2,3,4,5,6]

#insertion
#inserting 9 at index 3
L.insert(3,9)
print(L)  

#reversing a list
#with diffrent object using slicing
lnew =L[::-1]
print(lnew)

#inplace reversal
L.reverse()
print(L)

del lnew
print(lnew)
