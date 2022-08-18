def f(x):
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
		if len(positive)==0:
			final.append(negative[0])
			negative.pop(0)

		elif len(negative)==0:
			final.append(positive[0])
			positive.pop(0)
		
		elif j%2==0:
			final.append(positive[0])
			positive.pop(0)
		else:
			final.append(negative[0])
			negative.pop(0)


	print(final)

f([1,-9,2,-2,7,5,6,-4])