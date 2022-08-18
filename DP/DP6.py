def lcs(s1, s2):
	x, y=len(s1), len(s2)
	if x==0 or y==0:
		return 0
	key= s1, s2
	if key in dp:
		return dp[key]

	if s1[x-1]==s2[y-1]:
		dp[key]= 1+lcs(s1[:x-1], s2[:y-1])
		return dp[key]
	dp[key]=max(lcs(s1[:x-1], s2), lcs(s1, s2[:y-1]))
	return dp[key]


dp={}
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y))