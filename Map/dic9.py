str1 = 'w3resource' 

s={}

for i in str1:
	if i in s:
		s[i]=s[i]+1

	else:
		s[i]=1

print(s)