def prefix(s):
	a=s[0] #flower
	x=''
	for i in range(len(a)):
		for k in range(1,len(s)):
			if a[i]!=s[k][i]:
				return x
		x=x+a[i]
			
	
		



print(prefix(["flower","flow","flight"]))
print(prefix(["dog","racecar","car"]))