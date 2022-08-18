def truncate(s,k):
	x=list(s.split())

	c=x[:k]
	c=' '.join(c)
	return c 




print(truncate('what is your name' ,3))