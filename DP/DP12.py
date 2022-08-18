def MatrixSum(arr, i, j, sumz):
	if i==0 and j==0:
		return sumz
	if i<0 or j<0:
		return float('inf')
	key=i, j, sumz
	if key in dp:
		return dp[key]
	dp[key]=min(MatrixSum(arr, i, j-1, sumz+arr[i][j-1]), MatrixSum(arr, i-1, j, sumz+arr[i-1][j]))
	return dp[key]

dp={}
arr=[
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]


print(MatrixSum(arr,len(arr)-1 ,len(arr[0])-1 , arr[len(arr)-1][len(arr[len(arr)-1])-1]))

