def capital(s):
	a=s.split()
	for i in a:
		if ord(i[0])>=97 and ord(i[0])<=122:
			y=chr(ord(i[0])-32)
			print(y+i[1:], end=' ')
		else:
			print(i, end=' ')

x='1abhishek 2triguu'
(capital(x))