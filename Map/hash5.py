def f(arr, n):
	d={}
	max_length=0
	curr_sum=0

	for i in range(n):
		curr_sum=curr_sum + arr[i]
		if arr[i]==0 and max_length==0:
			max_length=1

		if curr_sum in d:
			max_length=max(max_length, i-d[curr_sum])
		else:
			d[curr_sum]=i
	return max_length


print(f([15, -2, 2, -8, 1, 7, 10, 23], 8))