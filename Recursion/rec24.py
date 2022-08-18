def tri(l):
	if len(l)==1:
		print(l)
		return
	x=[]
	for i in range(len(l)-1):
		x.append(l[i]+l[i+1])
	tri(x)
	print(l)

tri([1,2,3,4,5])
tri([1])