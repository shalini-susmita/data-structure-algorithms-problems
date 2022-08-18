def substring(s,h):
	a=0
	for i in s:
		if i in h:
			a=a+1
	if a>0:
		return 'YES'
	return 'NO'







print(substring('cdca', 'abc'))
print(substring('ax', 'opo'))