def alpha(s):
	l=list(s.split())

	d={}
	x=[]
	for i in l:
		x.append(i[len(i)-1])
		d[i[len(i)-1]]=i[0:len(i)-1]

	x=sorted(x)
	for i in x:
		print(i,d[i], end=' ')

alpha('Myself2 Me1 I4 and3')








