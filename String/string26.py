def caser(s, n):
	p=''
	for i in s:
		if (ord(i)>=ord('A') and ord(i)<=ord('Z')) or (ord(i)>=ord('a') and ord(i)<=ord('z')):
			if (ord(i)-n>=ord('A') and ord(i)-n<=ord('Z')) or (ord(i)-n>=ord('a') and ord(i)-n<=ord('z')):
				x=chr(ord(i)-n)
				p=p+x
			else:
				p=
		else:
			p=p+i
	return p




print(caser('a miss you', 5))