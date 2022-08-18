def consecutive(s1, s2):
	result=''
	for x in range(len(s1)+1):
		for i in range(len(s1)):
			if s1[i:x] in s2:
				if len(s1[i:x])>len(result):
					result=s1[i:x]
	return result









print(consecutive('abhishek', 'abhishek'))