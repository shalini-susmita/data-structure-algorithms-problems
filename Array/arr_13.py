def f(x, y, z):
	for i in x:
		if i in y and i in z:
			print(i, end=' ')

f([1,2,5,8], [2,3,5,7,8], [1,3,5,8,9])