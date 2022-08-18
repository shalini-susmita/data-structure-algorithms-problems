def binary(s):
	
	x=0
	y=0
	for i in s:
		if int(i)==1:
			x=x+1
		elif int(i)==0:
			y=y+1
	if x>y:
		return 'true'
	return 'false'


print(binary('11000'))
print(binary('11001111'))
print(binary('1100'))
print(binary('011'))