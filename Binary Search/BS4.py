def binary_Search_first(liss,ele):
	start=0
	end=len(liss)-1
	mid=(start+end)//2
	while start<=end:
		if liss[mid]<ele:
			start=mid+1
		elif liss[mid]>ele:
			end=mid-1
		else:
			x=mid
			end=mid-1
		mid=(start+end)//2
	return x

def binary_search_end(liss, num):
	start=0
	end=len(liss)-1
	mid=(start+end)//2
	while start<=end:
		if liss[mid]<num:
			start=mid+1
		elif liss[mid]>num:
			end=mid-1
		else:
			x=mid
			start=mid+1
		mid=(start+end)//2
	return x

def binary_search_occ(liss, ele):
	return binary_search_end(liss, ele)-binary_Search_first(liss, ele) + 1

print(binary_search_occ([20,30,30,30,30,30,30,40,50] , 30))
