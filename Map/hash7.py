def f1(s):
	a=0
	b=0
	for i in s:
		if i==1:
			a=a+1
		else:
			b=b+1
	return True if a==b else False

def f(x):
	max_size=0
	ind=-1,-1
	for l in range(len(x)+1):
		for i in range(len(x)-1-l):
			sub=x[i:i+l+1]
			if f1(sub)==False:
				continue
			if max_size<len(sub):
				max_size=len(sub)
				ind=i,i+l
	return max_size,ind


print(f([1,1,0,1,0,0,1,1,1,0,1,0]))