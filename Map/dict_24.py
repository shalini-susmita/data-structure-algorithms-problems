x=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

for i in x:
	for s in i:
		if i[s]=='#FF0000':
			x.remove(i)

print(x)
