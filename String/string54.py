def parenthesis(s):
	x=''
	d={')':'(', ']':'[', '}':'{'}

	for i in s:
		if x=='' and i not in list(d.values()):
			return 'false'
		elif i in list(d.values()):
			x=x+i
		elif x[len(x)-1]==d[i]:
			if len(x)==1:
				x=''
			else:
				x=x[0:len(x)-1]
	if x=='':
		return 'true'
	return 'false'

print(parenthesis('()'))
print(parenthesis('[({'))
print(parenthesis('[}(){]'))