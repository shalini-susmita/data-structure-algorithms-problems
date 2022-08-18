def f(x, l):
	ps=[x[0]]
	for i in range(1, len(x)):
		ps.append(ps[i-1] + x[i])


	for j in range(1, len(x)+1):
		for k in range(0, len(x)-j+1):
			end=ps[k-1] if k>0 else 0
			if ps[k+j-1]-end==l:
				return x[k:k+j]
			


print(f([3,7,4,11,10], 25))