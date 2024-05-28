#WAP print duplicates from a list of integers.
l =[1,2,3,4,2,3,2,1,1,8,7,6]
new_dict,new_list ={},[]
def dup(l):
    for i in l:
        if i not in new_dict:
            new_dict[i] =1
        else:
            new_dict[i]+=1

    for key,value in new_dict.items():
        if value>1:
            new_list.append(key)

    return new_list
