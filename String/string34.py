def binary(s):
	result=0
	len_0=0
	for i in s:
		if i=='0':
			len_0=len_0+1
		else:
			if len_0>result:
				result=len_0
			len_0=0


	return result





print(binary('1000100000001011000001'))