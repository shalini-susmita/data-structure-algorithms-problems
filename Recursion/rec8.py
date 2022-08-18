def sumdigits(n):
	if n==0:
		return 0
	return (n%10)+sumdigits(n//10)

print(sumdigits(8903))