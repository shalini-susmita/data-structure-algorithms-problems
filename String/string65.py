def ss(s):
	for i in range(len(s)):
		if s[0:i+1]*(len(s)//len(s[0:i+1]))==s:
			return 'true'


	return 'false'










print(ss('abcdaabcdaabcda'))
print(ss('abcabcabcabcabcabc'))