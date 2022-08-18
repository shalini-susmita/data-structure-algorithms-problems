def anagram(s1, s2):
	x=0
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
	for i in list(d1.keys()):
		if i not in d2.keys() or d1[i]!=d2[i]:
			return 'false' 
	return 'true'



print(anagram('cat', 'cog'))
print(anagram('cat', 'tac'))