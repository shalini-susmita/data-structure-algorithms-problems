def almost_equal(x,y):
	a=[]
	for i in range(len(x)):
		if x[i]!=y[i]:
			a.append(i)

	if len(a)==0:
		return True
	if len(a)==2:
		if x[a[0]]==y[a[1]] and x[a[1]]==y[a[0]]:
			return True
	return False

print(almost_equal('abcd','dbca'))
print(almost_equal('aaba','abba'))
print(almost_equal('abab','abab'))
