x={'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

mini=10000
for i in x:
	if len(x[i])<mini:
		mini=len(x[i])

for i in x:
	if len(x[i])==mini:
		print(i, end=',')



