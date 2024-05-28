#WAP to Find all duplicate characters in string .

def printdups(str):
    new_dict ={}
    for i in str:
        if i not in new_dict:
            new_dict[i] =1
        else:
            new_dict[i]+=1

    for key,value in new_dict.items():
        if value>1:
            print("character",key,"is repeated",value,"times")
printdups("hellojie")
