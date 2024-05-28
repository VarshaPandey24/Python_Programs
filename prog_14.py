#WAP using dictionary with keys having multiple inputs

#keys of dictionary with multiple inputs

places ={("1","2"):"delhi",("4","6"):"noida",("8","10"):"mumbai"}

lat=[]
lon =[]
plc =[]
for i in places:
    lat.append(i[0])
    lon.append(i[1])
    plc.append(places[i])

print(lat)
print(lon)
print(plc)
