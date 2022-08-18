x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for i in x:
	if i in y:
		if x[i]==y[i]:
			print(i, ':',  x[i])