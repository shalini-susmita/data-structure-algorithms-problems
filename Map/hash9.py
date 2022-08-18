# def f(s,low, high):
# 	x=[]
# 	s1=sorted(s)
# 	for i in range(low, high):
# 		if i not in s1:
# 			x.append(i)
# 	return x
def f(arr, low,high):
	x=[]
	l=0
	h=0
	for i in range(len(arr)): 
		if arr[i]==low:
			l=i 
		if arr[i]==high:
			h=i
		x=arr[l:h+1]
	return x

def f1(x, ele):
	star=0
	end=len(x)-1
	mid=(start+end)//2
	while start<=end:
		if liss[mid]<ele:
			start=mid+1
		elif liss[mid]>ele:
			end=mid-1
		else:
			return 1
		mid=(start+end)//2
	return 0

def f2(x):
	for i in range(low, high):
		if i not in  

low=12
high=16
print(f([10,13,12,16,18],low,high))