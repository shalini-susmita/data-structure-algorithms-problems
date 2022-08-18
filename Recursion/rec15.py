def findmax(liss):
	if len(liss)==1:
		return liss[0]
	return max(liss[0], findmax(liss[1:]))

print(findmax([1,7,87,3,4]))
print(findmax([-7,-41]))
