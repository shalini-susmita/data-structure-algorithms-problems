def f(x):
	max_end=0
	max_so_far=float('-inf')

	s, e = 0, 0

	for i in range(len(x)):
		max_end=max_end+ x[i]
		if max_so_far<max_end:
			max_so_far=max_end
			e=i

		if max_end< 0:
			max_end=0
			s=i+1

	return x[s:e+1]



print(f([8, -2, -10, 5, -4, 10, 0, -5]))