def alter(s):
	p='SOS'*(len(s)//3)
	a=0
	for i in range(len(s)):
		if s[i]!=p[i]:
			a=a+1
	return a

def alter1(s):
	return sum(1 for i in range(len(s)) if s[i]!=str('SOS'*(len(s)//3))[i])





print(alter1('SOSSPSSLSSOS'))