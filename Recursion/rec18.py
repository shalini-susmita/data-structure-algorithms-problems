def  evenodd(l,m):
	if l>m:
		return
	if l%2==0:
		print(l)
		evenodd(l+1,m)
	else:
		evenodd(l+1,m)
		print(l) 
	
print(evenodd(6,12))