def ind1(s):
	p=''
	for i in s:
		if i=='\n':
			p=p+i+'\t'
		else:
			p=p+i

	return p

def ind2(s):
	return s.replace('\n', '\n\t')

print(ind2('nlhlivhs\nlihfiha\necihhc\nefhouqehf'))

