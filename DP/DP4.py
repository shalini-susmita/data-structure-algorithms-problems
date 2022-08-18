def editDistance(str1, str2, m, n):
	global dp
	if m==0:
		return n 
	if n==0:
		return m
	key = m, n
	if key in dp:
		return dp[key]

	if str1[m-1]==str2[n-1]:
		dp[key] = editDistance(str1, str2, m-1, n-1)
		return dp[key]
		

	dp[key] = 1 + min(
		editDistance(str1, str2, m, n-1),
		editDistance(str1, str2, m-1, n-1),
		editDistance(str1, str2, m-1, n)
	)
	return dp[key]


dp = {}
str1='sunday'
str2='saturday'
print(editDistance(str1, str2, len(str1), len(str2)))
