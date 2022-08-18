sub={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

subx=[]
for l in range(0, len(list(sub.values())[0])):
	u={}
	for i in list(sub.keys()):
		u[i]=sub[i][l]
	subx.append(u)	
print(subx)
	
