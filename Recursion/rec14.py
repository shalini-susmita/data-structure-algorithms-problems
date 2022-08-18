def capital(s):
	if len(s)==0:
		return
	if s[0][0]>=chr(ord('A')) and s[0][0]<=chr(ord('Z')):
		print((s[0]))
	else:
		print(chr(ord(s[0][0])-32)+s[0][1:len(s[0])])

	return capital(s[1:len(s)])

capital(['cow', 'boy', 'Sun'])
capital([])