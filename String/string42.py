def love(s):
	a=0
	for i in range(len(s)//2):
		if s[i]!=s[len(s)-1-i]:
			z=ord(s[len(s)-1-i])-ord(s[i])
			a=a+abs(z)
	return a







print(love('abcde'))