def f1(s):
	a=[]
	for i in s:
		if i not in a:
			a.append(i)
	return len(a)


def f(arr):
	for i in range(len(arr)-1-x):
		sub=arr[i:i+x]
		print(f1(sub))


x=4
f([1,2,1,3,4,2,3,5])