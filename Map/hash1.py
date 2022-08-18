def f(ar1, ar2, m ,n):
	for i in range(n):
		for j in range(m):
			if ar2[i]==ar1[j]:
				break

		if j==m:
			return 0
	return 1


print(f([10, 9, 8, 34, 23], [9, 8,90], 5, 3))