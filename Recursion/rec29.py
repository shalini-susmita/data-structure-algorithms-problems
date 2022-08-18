def fiboo(n):
	if n>=0 and n==int(n):
		if n in [0,1]:
			return n
		return fiboo(n-1)+fiboo(n-2)

print(fiboo(9))