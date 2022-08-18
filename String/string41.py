def no_repeat(s):
	a=0
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			a=a+1
	return a





print(no_repeat('ABAAABBABABB'))
print(no_repeat('BBAABABBABABB'))
print(no_repeat('ABABBBAABBABABB'))
print(no_repeat('ABABABABABABABABAB'))