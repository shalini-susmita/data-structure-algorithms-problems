def double(s):
	a=''
	for i in range(len(s)):
		if a!='' and s[i]==a[len(a)-1]:
			a=a[0:len(a)-1]	
		else:
			a=a+s[i]

	if a=='':
		return 'empty'
	return a


print(double('abbaabbbaab'))