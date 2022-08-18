def f(x):
	a=[]
	b=[]
	for i in x:
		if i>=0:
			a.append(i)
		else:
			b.append(i)
	return [*a, *b]


print(f([1,-1,3,2,-7,-5,11]))