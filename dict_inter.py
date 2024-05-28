#converting lists into dictionaries with their frequencies

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

dict1={}
dict2={}
dict3 ={}
for i in ar1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1 

for i in ar2:
    if i not in dict2:
        dict2[i]=1
    else:
        dict2[i]+=1 

for i in ar3:
    if i not in dict3:
        dict3[i]=1
    else:
        dict3[i]+=1 


result_dict =dict(dict1.items() & dict2.items() & dict3.items())
print(result_dict)

common =[]
for (key,value) in result_dict.items():
    for i in range(0,value):
        common.append(key)
print(common)
 

