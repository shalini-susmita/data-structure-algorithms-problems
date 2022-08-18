def pal(s):
	z=''
	x=''
	for i in s:
		if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9'):
				z=z+i 
	for i in reversed(range(len(z))):
		x=x+z[i] 
	for i in range(len(z)):
		if z[i]!=x[i] and abs(ord(x[i])-ord(z[i]))!=32:
			return 'false'
	return 'true'




print(pal('A man, a plan, a canal: Panama'))
print(pal('race a car'))