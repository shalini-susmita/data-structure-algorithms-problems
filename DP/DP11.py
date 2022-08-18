def SumPartition(arr, i, s1, s2):
	if i==-1:
		return abs(s1- s2)
	key=i, s1, s2
	if key in dp:
		return dp[key]
	dp[key]=min(SumPartition(arr, i-1, s1+arr[i-1], s2), SumPartition(arr, i-1, s1, s2+arr[i-1]))
	return dp[key]



dp={}
s1=0
s2=0
arr=[10, 20, 15, 5, 25, 200, 80, 40, 21, 23]

print(SumPartition(arr, len(arr)-1, s1, s2))