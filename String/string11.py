def charachter(c):

	dic={}
	for i in c:
		keys=dic.keys()
		if i in keys:
			dic[i]=dic[i]+1
		else:
			dic[i]=1
	return dic

print(charachter('shalini susmita'))
