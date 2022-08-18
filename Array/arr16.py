def f(arr):
	if 0 in arr:
		return True
	for k in range(1, len(arr)+1):
		for i in range(len(arr)-k+1):
			sumz=0
			for j in range(i, i+k):
				sumz=sumz+arr[j]
			if sumz==0:
				return True
	return False


print(f([3,-8,2,-3, 6]))




