def f(x):
	p=0
	n=0
	positive=[]
	negative=[]
	final=[]
	for i in x:
		if i>=0:
			positive.append(i)
		else:
			negative.append(i)

	# print(positive)
	# print(negative)
	
	for j in range(len(x)):
		if p==len(positive):
			final.append(negative[n])
			n=n+1
		elif n==len(negative):
			final.append(positive[p])
			p=p+1
		elif j%2==0:
			final.append(positive[p])
			p=p+1
		else:
			final.append(negative[n])
			n=n+1

	print(final)

f([1,-9,2,-2,7,5,6,-4])