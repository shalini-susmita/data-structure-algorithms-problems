def SumMax(arr, i):
	global count
	if i==-1:
		return 0
	if i==0:
		return arr[0]
	if i==1:
		return arr[0] + arr[1]
	count=count+1
	key=i
	if key in dp:
		return dp[key]
	dp[key]=max(SumMax(arr, i-1), SumMax(arr, i-2)+arr[i], SumMax(arr, i-3)+ arr[i-1] + arr[i])
	return dp[key]


def Summax(arr, i):
	global countrec
	if i==-1:
		return 0
	if i==0:
		return arr[0]
	if i==1:
		return arr[0] + arr[1]
	countrec=countrec+1
	
	return max(Summax(arr, i-1), Summax(arr, i-2)+arr[i], Summax(arr, i-3)+ arr[i-1] + arr[i])


global count
global countrec
count=0
countrec=0
dp={}
arr=[100, 1000 ,100, 1000, 1, 100, 1000, 1, 100, 100, 1000 ,100, 1000, 1, 100, 1000, 1, 100]
print(SumMax(arr, 14))
print(Summax(arr, 14))
print(countrec)
print(count)
