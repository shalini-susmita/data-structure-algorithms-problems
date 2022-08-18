def dinner(s1,s2):
	a=0
	b=[]
	c={}
	mini=100000
	for i in range(len(s2)):
		c[s2[i]]=i

	for i in range(len(s1)):
		if s1[i] in s2:
			x=i+c[s1[i]]
		
			if x==mini:
				b.append(s1[i])
			elif x<mini:
				mini=x
				if len(b)==0:
					b.append(s1[i])
				else:
					b[0]=s1[i]
	return b

print(dinner(['a','b','c'] , ['c','n','l']))
print(dinner(['a','b','c'] , ['k','c','b']))