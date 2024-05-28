#to find number of negative an dpositive elements in a list
L=[2,4,-5,8,-7]

neg =0
pos =0
for i in range(0,5):
    if L[i]<0:
        neg+=1
    else:
        pos+=1    
print("positive:",pos)
print("negative:",neg)        