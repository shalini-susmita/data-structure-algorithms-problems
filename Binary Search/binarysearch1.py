def binary_search_last(liss, key):
	if key>liss[-1]:
		return key
	if key<liss[0]:
		return liss[0]
	start=0
	end=len(liss)-1
	mid=(start+end)//2
	while start<=end and start+1!=end:
		if liss[mid]<=key:
			start=mid
		else:   
			end=mid-1
		mid=(start+end)//2

	return liss[end]

x=int(input())
for i in range(x):
	listt=list(map(int, input().split()))
	key=int(input())
	print(binary_search_last(listt, key))



