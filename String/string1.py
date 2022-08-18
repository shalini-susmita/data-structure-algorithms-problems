def flip_case(c): 
	if ord(c)>=97 and ord(c)<=122:
		return chr(ord(c)-32)
	elif ord(c)>=65 and ord(c)<=90:
		return chr(ord(c)+32)
	else:
		return c
	
x=input()
l=''
for i in x:
	l=l+flip_case(i)
print(l)