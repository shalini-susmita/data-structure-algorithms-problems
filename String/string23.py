def reverse1(s):
	z=''
	for i in reversed(range(len(s))):
		z=z+s[i]
	return z

def reverse2(p):
	return p[len(p)-1::-1]

def reverse3(l):
	a=len(l)-1
	q=''
	while a>=0:
		q=q+l[a]
		a=a-1
	return q


	
s='asdf'
if len(s)%4==0:
	print(reverse3(s))
else:
	print(s)
