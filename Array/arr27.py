def f(x, a):
	for i in range(0, len(x)-2):
		for j in range(i+1, len(x)-1):
			for k in range(j+1, len(x)):
				if x[i] +x[j]+ x[k]==a:
					return True
	return False



print(f([1,3,6,2,7,9], 200))