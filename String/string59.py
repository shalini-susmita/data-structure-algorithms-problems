def vowels(a):
	z='aeiou'
	x=''
	y=''
	l=0
	for i in reversed(range(len(a))):
		if a[i] in z:
			x=x+a[i]
	for i in range(len(a)):
		if a[i] in z:
			y=y+x[l]
			l=l+1
		else:
			y=y+a[i]
	return y




print(vowels('hello'))
print(vowels('leetcode'))