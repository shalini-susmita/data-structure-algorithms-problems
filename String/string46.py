def funny(s):
	a=[]
	b=[]
	for i in range(len(s)-1):
		a.append(abs(ord(s[i])-ord(s[i+1])))
	for i in range(len(s)-1,0,-1):
		b.append(abs(ord(s[i])-ord(s[i-1])))
	if a==b:
		return 'funny'
	return 'not funny'	




print(funny('acxz'))
print(funny('bcxz'))