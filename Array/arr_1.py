def min_max(arr):
	mini=arr[0]
	maxi=arr[0]
	for i in range(len(arr)):
		if arr[i]<mini:
			mini=arr[i]
		if arr[i]>maxi:
			maxi=arr[i]
	print(mini)
	print(maxi)


min_max([8,-1,0,101])