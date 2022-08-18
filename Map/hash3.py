def f(l1,m ,l2, n):
	inter=[]
	union=[]
	for i in l1:
		if i in l2:
			inter.append(i)
	print('intersection list', inter)

	for i in range(m):
		union.append(l1[i])
		if l2[i] not in union:
			union.append(l2[i])
	print('union list', union)



f([10,14,9,3,2,1],6, [2,9,12,45,6,1],6)