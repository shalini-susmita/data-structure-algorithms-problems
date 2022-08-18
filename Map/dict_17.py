dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}

for i in list(dict1.keys()):
	if dict1[i]==None:
		dict1.pop(i)

print(dict1)
