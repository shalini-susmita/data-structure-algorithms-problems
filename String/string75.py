def chess(q):
	d={'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8'}
	s={}
	for i in list(d.keys()):
		for j in list(d.values()):
			if (int(d[i])%2!=0 and int(j)%2!=0) or (int(d[i])%2==0 and int(j)%2==0):
				s[i+j]='Black'
			else:
				s[i+j]='White'

	if s[q]=='Black':
		return False
	return True



print(chess('a2'))
print(chess('c5'))
print(chess('d7'))
