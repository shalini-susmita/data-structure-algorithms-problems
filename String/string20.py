def even(s):
	c=''
	for i in range(len(s)):
		if i%2==0:
			c=c+s[i]
	return c

print(even('djwdjpwqj'))