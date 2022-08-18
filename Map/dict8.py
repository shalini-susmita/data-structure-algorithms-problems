d ={'1':['a','b'], '2':['c','d'], '3':['e', 'f', 'g']}

x=list(d.values())[0]
y=list(d.values())[1]
z=list(d.values())[2]
for i in x:
	for j in y:
		for k in z:
			print(i+j+k)



