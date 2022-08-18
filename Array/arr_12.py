def f(x):
	d={}
	for i in x:
		d[i]=d.get(i, 0) +1
	for j in d:
		if d[j]>1:
			print(j, end=' ')
	

f([1,2,2,2,3,3,4,0])