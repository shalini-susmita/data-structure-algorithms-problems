def f(arr, n):
	d={}
	for i in range(n):
		for j in range(i+1, n):
			sumz=arr[i] +arr[j]

			if sumz in d:
				print(d[sumz],'and', (arr[i], arr[j]))
				return
			else:
				d[sumz]=arr[i], arr[j]



f([3,4,7,1,2,9,8], 7)