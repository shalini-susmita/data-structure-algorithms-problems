def lis(arr):
	n=len(arr)
	lis=[1]*n
	for i in range(1, n):
		for j in range(0, i):
			if arr[j]<arr[i]:
				lis[i]= max(lis[i], 1+lis[j])
	return max(lis)



arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", lis(arr))