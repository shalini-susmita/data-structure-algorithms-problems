def Sherlock(s):
	a={}
	e={}
	for i in s:
		if i in a:
			a[i]=a[i]+1
		else:
			a[i]=1
	x=list(a.values())
	for i in x:
		if i in e:
			e[i]=e[i]+1
		else:
			e[i]=1

	if len(e.keys())>2:
		return 'NO'
	if len(e.keys())==1:
		return 'YES'
	p=list(e.values())

	if p[0]>1 and p[1]>1:
		return 'NO'
	l=list(e.keys())
	if abs(l[0]-l[1])>1:
		return 'NO'
	return 'YES'

print(Sherlock('aabbcdd')) 
print(Sherlock('aabbccddeefghi'))