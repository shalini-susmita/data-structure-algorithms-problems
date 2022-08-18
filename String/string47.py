def anagram(s):
	a=len(s)//2
	x={}
	y={}
	w=0
	for i in range(0, a):
		if s[i] in x:
			x[s[i]]=x[s[i]]+1
		else:
			x[s[i]]=1

	for i in range(a, len(s)):
		if s[i] in y:
			y[s[i]]=y[s[i]]+1
		else:
			y[s[i]]=1
	for i in x.keys():
		if i in y and x[i]<y[i]:
			w=w+0
		elif i not in y:
			w=w+x[i]
		else:
			w=w+(x[i]-y[i])


	return w
print(anagram('fdhlvosfpafhalll'))	