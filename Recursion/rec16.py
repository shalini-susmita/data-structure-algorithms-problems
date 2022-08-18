def nod(n):
	if n//10==0:
		return 1
	return 1+nod(n//10)

print(nod(34567))