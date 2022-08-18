def pali(n):
	if len(n)==0 or len(n)==1:
		return True
	if n[0]!=n[-1]:
		return False
	return pali(n[1:len(n)-1])

print(pali('tacocat'))
print(pali('tacoca'))