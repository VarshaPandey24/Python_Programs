def recursivedeletion(text,pattern):
    if len(text)==0 and len(pattern)==0:
        return True
    
    while(len(text)!=0):
        #finding index of pattern
        index  =text.find(pattern)

        if index==-1:
            return False
        else:
            text =text[0:index]+text[index+len(pattern):]
    return True    