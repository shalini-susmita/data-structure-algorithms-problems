num=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

for i in num:
	for z in i:
		i[z]=float(i[z])

print(num)