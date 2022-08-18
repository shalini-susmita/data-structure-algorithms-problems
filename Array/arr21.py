def f(x):
	sumz=0
	for i in range(len(x)):
		sumz=sumz + (i*x[i])
	return sumz

def f1(z):
	sum_=f(z)
	a=z
	for j in range(len(z)):
		x=[]
		for i in range(1,len(a)):
			x.append(a[i])
		x.append(a[0])
		sum_=max(sum_, f(x))
		a=x
	return sum_




print(f1([8,3,1,2]))