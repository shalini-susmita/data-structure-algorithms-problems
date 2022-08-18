def binary(l,x,start,end):
	mid=(start+end)//2
	if x>l[mid]:
		return binary(l,x,start=mid+1,end=end)
	elif x<l[mid]:
		return binary(l,x,start=start,end=mid-1)
	else:
		return mid
	if start==end:
		return 'not found'

print(binary([8,17,90,809,78090],8,0,4))