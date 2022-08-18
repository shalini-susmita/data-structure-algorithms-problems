def sumz_diagonal(arr, i,j,sumi):
	end_x=len(arr)-1
	end_y=len(arr[len(arr)-1])-1
	if i>end_x  or j>end_y:
		return float('inf')

	if i==end_x and j==end_y:
		return sumi+arr[end_x][end_y]

	return min(sumz_diagonal(arr, i, j+1, sumi+arr[i][j]), sumz_diagonal(arr, i+1, j , sumi+arr[i][j]))


arr=[
	[1,2,3], 
	[2,3,4], 
	[-1,0,2]
]

print(sumz_diagonal(arr,0,0,0))