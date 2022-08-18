def fibonacci(n):
	if n>=0 and n==int(n):
		if n in [1,2]:
			return n-1
		else:
			return fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(6))
