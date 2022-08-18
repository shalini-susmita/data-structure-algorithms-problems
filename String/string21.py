def freq(s):
	o={}
	x=s.split()
	for i in x:
		if i in o:
			o[i]=o[i]+1
		else:
			o[i]=1
	return o

print(freq('the dog name is the marvel is the dog'))