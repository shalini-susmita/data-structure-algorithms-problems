def f(x):
	max_=0
	for i in range(len(x)-1):
		for j in range(i+1, len(x)):
			if x[j]-x[i]>max_:
				max_=x[j]-x[i]

	return max_



print(f([4,3,7,8]))
