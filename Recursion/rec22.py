def kutta(i):
	print(i,end=' ')
	if i==1:
		return
	if i%2==0:
		return kutta(i//2)
	elif i%2!=0:
		return kutta(i*3+1)

kutta(6)