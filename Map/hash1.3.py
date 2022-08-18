def f(l1, m, l2, n):
	d={}
	for i in range(m):
		if l1[i] not in d:
			d[l1[i]]=i
	for i in range(n):
		if l2[i] not in d:
			return 0
	return 1






print(f([10,5,2,89,76], 5, [5,2,22], 3))