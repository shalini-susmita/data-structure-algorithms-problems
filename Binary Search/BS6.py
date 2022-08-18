# def sum_unsorted(liss, ele):

# 	for i in range(0, len(liss)):
# 		for j in range(i+1, len(liss)):
# 			if liss[i]+liss[j]==ele:
# 				return True
# 	return False

# print(sum_unsorted([2,3,4,6], 10))
# print(sum_unsorted([2,3,4,6], 12))
# print(sum_unsorted([2,3,4,1], 6))

def sum_soreted(liss,x):
	start=0
	end=len(liss)-1
	while start<end:
		if liss[start]+liss[end]<x:
			start=start+1
		elif liss[start]+liss[end]>x:
			end=end-1
		else:
			return True

	return False

print(sum_soreted([1,2,3,4,5], 7))

print(sum_soreted([1,2,3,4,5], 10))