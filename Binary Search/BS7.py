def merge_sorted_lists(liss1,liss2):
	sorted_liss=[]
	i, j=0, 0
	while i<len(liss1) and j<len(liss2):
		if liss1[i]<liss2[j]:
			sorted_liss.append(liss1[i])
			i=i+1
		else:
			sorted_liss.append(liss2[j])
			j=j+1
	while i< len(liss1):
		sorted_liss.append(liss1[i])
		i=i+1
	while j< len(liss2):
		sorted_liss.append(liss2[j])
		j=j+1

	return sorted_liss

def merge_sort(liss):
	if len(liss)==1:
		return liss 
	mid=len(liss)//2
	L=liss[:mid]
	R=liss[mid:]
	left = merge_sort(L)
	right = merge_sort(R)
	return merge_sorted_lists(left, right)


print(merge_sort([5,4,1,2,7,12,9,4,3,1]))
