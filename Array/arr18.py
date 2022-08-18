def f(x):
	pre_sum=0
	sumz=0
	for i in range(len(x)):
		pre_sum=pre_sum+x[i]
	
	for i in range(1, len(x)+1):
		for j in range(0, i-1):
			if j<0:
				sumz=pre_sum[j+i-1] - pre_sum[j]

			else:
				pre_sum[j+i-1]- pre_sum[j-1]==0:
			return True
	return False




print(f([2,1,-4,4,0]))