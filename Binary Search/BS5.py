def binary_search_peak(liss):
	start=0
	end=len(liss)-1
	mid=(start+end)//2
	if liss[0]>liss[1]:
		return liss[0]
	elif liss[len(liss)-1]>liss[len(liss)-2]:
		return liss[len(liss)-1]
	while start<=end:
		if liss[mid]>=liss[mid+1] and liss[mid]>=liss[mid-1]:
			return liss[mid]
		elif liss[mid]<liss[mid+1]:
			start=mid+1
		elif liss[mid]<liss[mid-1]:
			end=mid-1
		return liss[mid]
		mid=(start+end)//2


print(binary_search_peak([6,4,3]))
