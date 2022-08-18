def binary(n, s):
	a=0
	x='010'
	i=0
	while i<(len(s)-2):
		if s[i:i+3]==x:
			a=a+1
			i=i+3
		else:
			i=i+1

	return a
	




print(binary(7, '10101010101'))
