def rodCut(price, n):
	if n==0:
		return 0
	max_value=-10000
	for i in range(1, n+1):
		cost=price[i-1] + rodCut(price, n-i)
		if cost>max_value:
			max_value=cost
	return max_value

def rodCutDP(price, n):
	global dp
	if n==0:
		return 0
	if n in dp:
		return dp[n]
	max_value=-10000
	for i in range(1, n+1):
		cost=price[i-1] + rodCutDP(price, n-i)
		if cost>max_value:
			max_value=cost
	dp[n]=max_value
	return dp[n]

dp={}
price = [1, 5, 8, 9, 10, 17, 18, 20]
n = 8
print('Profit is', rodCut(price, n))
print('Profit is', rodCutDP(price, n))
print('Recursive:', count)
print('DP:', count_dp)