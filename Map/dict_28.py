even={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}


for i in even:
	for z in even[i]:
		if z%2!=0:
			even[i].remove(z)

print(even)
