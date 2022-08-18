def substring(s):
	a=0
	for i in range(0,len(s)-3):
		p=s[i:i+3]
		q=''
		for g in p:
			if g not in q:
				q=q+g
		if p==q:
			a=a+1
	return a 

print(substring('xyzzaz'))
print(substring('aababcabc'))