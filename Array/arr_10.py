def f(x, n):
	y=sorted(x)
	if y[0]!=1:
		return 1
	for i in range(len(y)-1):
		if y[i+1]-y[i] !=1:
			return y[i]+1


print(f([6,10,4,3,5,2,1,8,9], 10))
