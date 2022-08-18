def productarray(x):
	if len(x)==1:
		return x[0]
	return x[0]*productarray(x[1:len(x)])

print(productarray([2,3,4,1]))