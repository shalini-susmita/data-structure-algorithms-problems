def binarysearch(l, x):
	start=0
	end=len(l)-1
	while start!=end:
		mid=(start+end)//2
		if x>l[mid]:
			start=mid+1
		elif x<l[mid]:
			end=mid-1
		else:
			return mid
	return 'not found'

print(binarysearch([34,56,89,100,3890],38900))

