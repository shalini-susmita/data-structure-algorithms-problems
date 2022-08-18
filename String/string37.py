def word(s):
	x=s.split()
	large=0
	small=10000
	l=''
	c=''
	for i in x:
		if len(i)>large:
			large=len(i)
			l=i
		if len(i)<small:
			small=len(i)
			c=i


	print(l, c) 


word('the shalini susmita is a good girl')