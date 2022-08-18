def rec5(n):
	if n>10:
		return
	print('11 X ',n, ' = ', 11*n, sep='')
	rec5(n+1)

def rec6(n):
	if n<1:
		return
	rec6(n-1)
	print('11 X ',n, ' = ', 11*n, sep='')

rec6(10)

# rec5(1)