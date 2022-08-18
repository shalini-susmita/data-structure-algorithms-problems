def bs(liss):
	start=0                       
	end=len(liss)-1
	mid=(start+end)//2
	while start<=end and liss[mid]<liss[mid+1]:
		if liss[mid]<liss[0]:
			end=mid-1
		elif liss[mid]>liss[0]:
			start=mid+1

		mid=(start+end)//2
	return mid+1

def binary_search(liss, ele):
	start=0
	end=len(liss)-1
	mid=(start+end)//2
	while start<=end:
		if liss[mid]<ele:
			start=mid+1
		elif liss[mid]>ele:
			end=mid-1
		else:
			return mid
		mid=(start+end)//2

def bs1(liss, ele):

	p=bs(liss)
	left_subarray=liss[0:p]
	right_subarray=liss[p:]

	if ele<liss[0]:
		return p + binary_search(right_subarray, ele)
		
	else:
		return binary_search(left_subarray, ele)

print(bs1([3,4,5,6,1,2], 1))
	
	


