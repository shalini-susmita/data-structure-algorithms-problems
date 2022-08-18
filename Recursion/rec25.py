def stringrev(s):
	if len(s)==1:
		return s
	return stringrev(s[1:])+s[0]



print(stringrev('cat'))