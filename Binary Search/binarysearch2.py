# To find frequency of any number in [1,2,3,7,7,7,7,7,7,8,9,23]


def binary_search_first(liss, ele):
	start=0
	end=len(liss)-1
	mid=(start+end)//2
	while start<=end and start+1!=end:
		if liss[mid]<ele:
			start=mid+1
		elif liss[mid]>=ele:
			end=mid
		mid=(start+end)//2
	return end

def binary_search_last(liss, ele):
	start=0
	end=len(liss)-1
	mid=(start+end)//2
	while start<=end and start+1!=end:
		if liss[mid]<=ele:
			start=mid
		elif liss[mid]>ele:
			end=mid-1		
		mid=(start+end)//2
	return start

liss=[3,7,7,7,7,7,7,7,7,8]

x=binary_search_first(liss,7)
y=binary_search_last(liss,7)

print(y-x+1)