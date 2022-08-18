def f(x, k):
	a=0
	for i in range(len(x)-1):
		for j in range(i+1, len(x)):
			if x[i]+x[j]==k:
				a=a+1
	return a 

print(f([1,1,1,1], 2))