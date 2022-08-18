def isomorphic(s1,s2):
	d1={}
	d2={}
	for i in s1:
		if i in d1:
			d1[i]=d1[i]+1
		else:
			d1[i]=1
	for i in s2:
		if i in d2:
			d2[i]=d2[i]+1
		else:
			d2[i]=1
	x=list(d1.values())
	y=list(d2.values())
	if sorted(x)==sorted(y):
			return 'true'
	return 'false'




print(isomorphic('egg', 'add'))
print(isomorphic('foo', 'bro'))
print(isomorphic('oho', 'hoo'))