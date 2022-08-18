def peak_element(x):
	if x[0] >= x[1]:
		return 0
	if x[len(x)-1] >= x[len(x)-2]:
		return len(x)-1
	for i in range(len(x)-1):
		if x[i]>=x[i+1] and x[i]>=x[i-1]:
			return i		

print(peak_element([1,2,3,4,5]))
print(peak_element([3,4,1,6,7,9,4,1])) 