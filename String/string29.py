def rev2(s):	
	e=''
	for i in range(len(s)-1,-1, -1):
		e=e+s[i]
	return e


def reverse1(s):
	x=s.split(' ')
	a=''
	for i in x:
		a=a+rev2(i)+' '
	return a


print(reverse1('hello Ehsaas how are you'))

