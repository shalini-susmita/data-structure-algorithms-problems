def ss(s):
	if len(set(s))==len(s):
		return True:
	return False

def swap(x,y):
	a=[]
	b=[]

	for i in range(len(y)):
		if y[i]!=x[i]:
			a.append(y[i])
			b.append(x[i])

	for i in range(len(a)):
		if len(a)==2:
			if a[0]==b[1] and a[1]==b[0]:
				return True
		
	return False

print(swap('aaabc', 'aaacb'))
print(swap('ab', 'ab'))
print(swap('aaaa', 'aaaa'))
print(swap('aaabaac', 'aaacaab'))







