def case(a,b):
	if b==chr(ord(a)+32) or b==chr(ord(a)-32):
		return True
	return False


def great_string(s):
	n=''
	i=0
	while i<(len(s)):
		if i==len(s)-1 or case(s[i], s[i+1])==False:
			if n!='' and case(s[i],n[-1])==True:
				n=n[0:len(n)-1] if len(n)>1 else ''
			else:
				n=n+s[i]
			i=i+1
		else:
			i=i+2
	return n

print(great_string('abBcCA'))


