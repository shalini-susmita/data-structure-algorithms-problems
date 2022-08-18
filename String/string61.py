def left_shift(s):
	c=''
	x=s[1:len(s)]+s[0]
	c=c+x
	return c

def goal(t,g):
	if t==g:
		return 'true'
	
	n=len(t)
	k=n-1
	new_string=t
	i=0
	while i<k:
		new_string=left_shift(new_string)
		if new_string==g:
			return 'true'
		i=i+1
	return 'false'

print(goal('abcde', 'bcdea'))
print(goal('abcde', 'bdace'))

