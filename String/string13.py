def replace_charc(s):
	c=s[0]
	
	for i in range(1, len(s)):
		
		if s[i]==s[0]:
			c=c+'$'
		else:
			c=c+s[i]

	return c

print(replace_charc('susmita'))