def backspace(s):
	z=''
	for i in range(len(s)):
		if s[i]!='#':
			z=z+s[i]
		else:
			z=z[0:len(z)-1]
	return z
def bs(a,b):
	p=''
	q=''
	p=backspace(a)
	q=backspace(b)
	if p==q:
		return True
	return False


print(bs('ab#c', 'ad#c'))
print(bs('a#b##c', 'ad#c'))
print(bs('#c', 'ad#c'))		





