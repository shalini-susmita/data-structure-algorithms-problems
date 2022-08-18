def isconsonant(c):
	a=['a','e','i','o','u','A','E','I','O','U']
	if c not in a and ((ord(c)>=ord('a') and ord(c)<=ord('z')) or (ord(c)>=ord('A') and ord(c)<=ord('Z'))):
		return True
	return False

def conso(s):
	if len(s)==1:
		if isconsonant(s)==True:
			return 1
		return 0
	if isconsonant(s[0])==True:
		return (1+conso(s[1:]))
	return conso(s[1:])

print(conso('My name is Ehsaas' ))
print(conso('M'))
