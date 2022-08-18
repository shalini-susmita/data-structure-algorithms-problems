def odd(s):
	x=-1
	for i in range(len(s)):
		if int(s[i])%2!=0:
			x=i
	if x==-1:
		return '""'
	return s[0:x+1]






print(odd('34567'))
print(odd('890'))
print(odd('22'))