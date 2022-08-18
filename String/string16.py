def custom_replace(s, t, r):
	c=''
	i=0
	while i<len(s) :
		if s[i:i+len(t)]==t:
			c=c+r
			i=i+len(t)
		else:
			c=c+s[i]
			i=i+1		

	return c





# print(custom_replace('i am not that poor but then he is also not that poor and that I know well', 'not that poor', 'good'))
print(custom_replace('i am not', 'am', 'toy'))