even={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

num={}
for i in even:
	num[i] = []
	for z in even[i]:
		if z%2==0:
			num[i].append(z)
print(num)