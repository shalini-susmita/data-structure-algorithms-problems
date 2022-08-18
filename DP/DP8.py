def LPS(seq, x, y):
	if x==y:
		return 1
	if y==x+1 and seq[x]==seq[y]:
		return 2
	key=x,y
	if key in dp:
		return dp[key]
	if seq[x]==seq[y]:
		dp[key]=2+ LPS(seq, x+1, y-1)
		return dp[key]
	dp[key]=max(LPS(seq, x+1, y), LPS(seq, x, y-1))
	return dp[key]

dp={}
seq='GEFEG'
print(LPS(seq, 0, len(seq)-1 ))
