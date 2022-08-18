def ss(s):
	i=0
	z=0
	while i<=len(s)-1:
		x=i
		y=''
		while x<=len(s)-1:
			if s[x] not in y:
				y=y+s[x]

			else:
				break
			x=x+1
		if len(y)>z:
			z=len(y)
		i=i+1
	return z

print(ss('abcabcbb'))
print(ss('abcdefghijkl'))
print(ss('abbcdefgh'))