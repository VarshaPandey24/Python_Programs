#merging two dictionaries
#using update method

def merge(dict1,dict2):
    dict3 =dict1.update(dict2)

#without built-in methods

def merges(dict1,dict2):
    for i in dict1.keys():
        dict2[i]=dict1[i]    
    return dict2    