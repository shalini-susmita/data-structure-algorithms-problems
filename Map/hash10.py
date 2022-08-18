def f(s):
	for i in range(1,len(s)+1):
		for j in range(len(s)-1-i):
			for k in range(j, j+i):
				print((s[k]))
				

f([6,3,-1,-3,4,-2,2,4,6,-12,-7])