def swap(x,y):
	x1=x[:2] + y[2:]
	y1=y[:2] + x[2:]

	return x1+' '+ y1

print(swap('shalini', 'susmita'))