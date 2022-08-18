def knapsack1(W, wt, val, i):
	global c
	if i<0 or W==0:
		return 0
	c=c+1
	key=W, i
	if key in dp:
		return dp[key]

	dp[key]=max(val[i]+ knapsack1(W-wt[i] , wt, val, i-1), knapsack1(W, wt,val, i-1))
	return dp[key]


def knapsack(W, wt, val, i):
	global c1
	if i<0 or W==0:
		return 0
	c1=c1+1
	
	return max(val[i]+ knapsack(W-wt[i] , wt, val, i-1), knapsack(W, wt,val, i-1))
	

global c1
global c
c=0
c1=0
dp={}
val = [60, 100, 120, 45,22,78,12,3,4, 60, 100, 120, 45,22,78,12,3,4]
wt = [10, 20, 30, 40,50,60,70,80,90, 10, 20, 30, 40,50,60,70,80,90]
W = 700
i=len(val)-1

print(knapsack1(W,wt,val,i))
print(knapsack(W,wt,val,i))
print(c)
print(c1)