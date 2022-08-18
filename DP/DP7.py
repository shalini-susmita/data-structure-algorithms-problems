
def ss(arr, n, sum_):
	if sum_==0:
		return True
	if n==0:
		return False
	
	return ss(arr, n-1, sum_) or ss(arr, n-1, sum_-arr[n-1])
	


def ss1(arr, n, sum_):
	if sum_==0:
		return True
	if n==0:
		return False
	global dp
	key=n, sum_
	if key in dp:
		return dp[key]

	dp[key]=ss1(arr, n-1, sum_) or ss1(arr, n-1, sum_-arr[n-1])
	return dp[key]
	

dp={}
arr = [3, 4, 3, 4, 12, 5, 3, 5, 4, 2]
sum_ = 7
n = len(arr)
print(ss(arr, n, sum_))
print(ss1(arr, n, sum_))







