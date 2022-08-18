def f(x):
	z=1
	maxz=0
	q=[]
	for i in x:
		if i not in q:
			q.append(i)
	
	a=sorted(q)
	for i in range(len(a)-1):
		if a[i+1]- a[i]==1:
			z=z+1

		else:
			if z>maxz:
				print(maxz, z)
				maxz=z
			z=1

	print(max(z, maxz))

f([1,2,3,12,13, 14, 78, 79, 80, 81, 82, 83])