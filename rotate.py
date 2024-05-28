#to rotate a string 

def rotate(text,d):

    #left rotation
    lfirst =text[d:]
    lsecond =text[0:d]
    textLeft =lfirst+lsecond
    print("left rotation by ",d,"position is ",textLeft)

    #right rotation
    rfirst =text[0:len(text)-d]
    rsecond =text[len(text)-d:]
    textright =rsecond+rfirst
    print("right rotation by",d,"position is",textright)
rotate("hello",3)
