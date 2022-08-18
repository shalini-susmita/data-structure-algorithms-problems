sub=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
c=[]
for i in sub:
	for z in i:
		if z=='Math':
			c.append(i[z])

print(c)

