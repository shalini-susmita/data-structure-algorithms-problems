def rev(arr):
	x=[]
	for i in range(len(arr)-1, -1, -1):
		x.append(arr[i])

	print(x)

rev([0,2,3,4])