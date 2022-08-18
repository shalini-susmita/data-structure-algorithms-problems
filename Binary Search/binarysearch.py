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
			print('Element found at position', mid)
			return
		mid=(start+end)//2
	print('element not found')

binary_search([2,6,7,8,9,90],6)

#######################################################################

num=64

start=1
end=num
mid=(start+end)//2

while start<=end:
	if mid*mid<=num:
		start=mid+1
	elif mid*mid>=num:
		end=mid-1
	else:
		print('square root is', mid)
		break
	mid=(start+end)//2





