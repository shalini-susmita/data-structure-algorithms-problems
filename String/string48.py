def angram(s,z):
	p={}
	q={}
	a=0
	g=0
	for i in s:
		if i in p:
			p[i]=p[i]+1
		else:
			p[i]=1
	for i in z:
		if i in q:
			q[i]=q[i]+1
		else:
			q[i]=1
	for i in p.keys():
		if i in z and p[i]<z[i]:
			a=a+0
		elif i not in z:
			a=a+p[i]
		else:
			a=a+p[i]-z[i]
	for i in z.keys():
		if i in p and z[i]<p[i]:
			a=a+0
		elif i not in p:
			a=a+z[i]
		else:
			a=a+z[i]-p[i]			


	return a

print(angram('abck', 'aaabbc'))