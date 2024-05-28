l=[(1,2),(3,4),(2,0)]
dict ={}

for key,val in l:
    dict.setdefault(key,val)
print(dict)    