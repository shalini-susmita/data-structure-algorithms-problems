def f(x):
	d={}
	for i in (x):
 		d[i]=d.get(i, 0)+1
	

	for j in range(len(x)):
		if d[x[j]]>1:
			return j	
		

print(f([1,2,3,3,5,5,6,]))
                                                                                                  