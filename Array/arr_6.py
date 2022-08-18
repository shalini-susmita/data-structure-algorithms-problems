def freq(x, n):
	a=0
	for i in x:
		if i==n:
			a=a+1

	return a 

print(freq([2,3,3,3,4,5], 3))