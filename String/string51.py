def dollar(s):
	p=''
	a=0
	for i in s:
		if i not in p:
			a=a+1
		p=p+i
	return a



print(dollar('abcd'))
print(dollar('abab'))