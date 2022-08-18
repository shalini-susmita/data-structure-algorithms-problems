def sumpartition(arr, i, sum):
	if sum==0:
		return True
	if i<0:
		return False
	return sumpartition(arr, i-1, sum) or sumpartition(arr, i-1, sum-arr[i])


def printsets(set1, set2):
	for i in range(len(set1)):
		print(set1[i], end=' ')
	print()

	for i in range(len(set2)):
		print(set2[i] , end=' ')

def findset(arr,set1, set2, s1, s2, i):
	if i==len(arr):
		if s1==s2:
			printsets(set1, set2)
			return True
		else:
			return False
	set1.append(arr[i])
	fs=findset(arr, set1, set2, s1+arr[i] , s2, i+1)
	if fs:
		return True
	set1.pop()
	set2.append(arr[i])

	fs=findset(arr, set1, set2, s1, s2+arr[i], i+1)
	if not fs:
		set2.pop()
	return fs


set1=[]
set2=[]
arr=[5,1,6]
s1=0
s2=0
# for i in arr:
# 	s=s+i
# if s%2!=0:
# 	print(False)

print(findset(arr, set1, set2, s1, s2, 0))