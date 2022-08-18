def plate(s, l):
	a=0
	maxi=0
	v=''
	for i in l:
		a=0
		for k in i:
			if k in s or chr(ord(k)+32) in s or chr(ord(k)-32) in s:
				a=a+1
		if a>=maxi:
			maxi=a
			v=i
	return v




print(plate('OgEu755', ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]))