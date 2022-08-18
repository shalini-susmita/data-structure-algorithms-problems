def consecutive(s):
	a=s[0]
	for i in s[1:]:
		if a[len(a)-1]!=i:
			a=a+i


	return a


print(consecutive('abbbbccaa'))