color={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

col={}
for i in color:
	col[color[i]]=len(color[i])

print(col)
