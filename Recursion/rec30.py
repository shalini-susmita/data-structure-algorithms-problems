def productii(l):
	if len(l)==1:
		return l[0]
	return l[0]*productii(l[1:len(l)])

print(productii([8,2,7,1]))