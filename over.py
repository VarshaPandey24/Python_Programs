#function overloading 
def sum(*args):
	result =0
	for num in args:
		result+=num
	return result	
	
print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,4))
print(sum(1,2,69))


