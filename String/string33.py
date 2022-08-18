def repeat1(s):
	d={}
	x=s.split()
	for i in x:
		if i in d:
			d[i]=d[i]+1
		else:
			d[i]=1

	a=sorted(d.values())
	for i in d:
		if d[i]==a[-2]:
			print(i)



repeat1('i am shalini i i am am am shalini jhiokl pioli')

