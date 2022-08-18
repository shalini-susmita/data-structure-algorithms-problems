def f(x):
	min_ele=x[0]
	max_=x[1]-x[0]

	for i in range(1, len(x)):
		if x[i]- min_ele>max_:
			max_=x[i]- min_ele

		if x[i]<min_ele:
			min_ele=x[i]
	return max_


print(f([2,4,3,5,6,8]))