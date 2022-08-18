def prefix(s, k):
	p=k
	for i in range(len(s)):
		if s[i]=='\n' and i!=len(s)-1:
			p=p+s[i]+k
		else:
			p=p+s[i] 
	return p


print(prefix('nvonoerv\nkjkdliqhdl\nlhedhcfle\n' , '$'))



