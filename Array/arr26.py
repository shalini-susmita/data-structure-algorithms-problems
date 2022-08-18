def f(arr, dep, n):
	plat=1
	res=1
	for i in range(n):
		plat=1
		for j in range(i+1, n):
			if arr[i] <arr[j] and dep[i]> arr[j] or arr[j]>arr[i] and dep[i]> arr[j] :
				plat=plat+1
		res=max(res, plat)

	return res

print(f([900, 1100, 1235], [1000, 1200, 1240], 3))