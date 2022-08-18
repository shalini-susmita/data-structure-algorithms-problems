def coin(arr, n, sumz):
	global c 
	if sumz==0:
		return 1
	if sumz<0:
		return 0
	if n<0:
		return 0
	c=c+1
	return coin(arr, n-1, sumz) + coin(arr, n, sumz-arr[n]) 



def coin_DP(arr, n, sumz):
	global c 
	if sumz==0:
		return 1
	if sumz<0:
		return 0
	if n<0:
		return 0
	c=c+1
	key= n, sumz
	if key in dp:
		return dp[key]
	dp[key]=coin(arr, n-1, sumz) + coin(arr, n, sumz-arr[n])
	return dp[key] 

dp={}
coins=[1,2,3]
global c
c=0

print(coin_DP(coins, len(coins)-1, 4))
print(c)





