def GOT(s):
	x={}
	a=0
	for i in s:
		if i in x:
			x[i]=x[i]+1
		else:
			x[i]=1
	for i in x.values():
		if i%2!=0:
			a=a+1
	if a>1:
		return 'NO'
	return 'YES'		

print(GOT('cdefghmnopqrstuvw'))
print(GOT('cdcdcdcdeeeef'))