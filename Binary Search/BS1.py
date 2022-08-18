# def bs(liss,s):
# 	start=0
# 	end=len(liss)-1
# 	mid=(start+end)//2
# 	while start<=end:
# 		if liss[mid]>s:
# 			end=mid-1
# 		elif liss[mid]<s:
# 			start=mid+1
# 		else:
# 			print('element found at', mid)
# 			return
# 		mid=(start+end)//2
# 	print('element not found')

# bs([4,5,6,7,8,9,10], 4)

# *******************************************************
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