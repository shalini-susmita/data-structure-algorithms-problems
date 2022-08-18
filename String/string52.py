def Sherlock(s):
	a={}
	x=0
	for i in s:
		if i in a:
			a[i]=a[i]+1
		else:
			a[i]=1
	b=list(set(list(a.values())))
	if len(b)>2:
		return 'NO'
	
	if abs(b[0]-b[1])<=1:
		return 'YES'
	return 'NO'


print(Sherlock('aabbccddeefghi')) 
print(Sherlock('aabbccccdd'))
