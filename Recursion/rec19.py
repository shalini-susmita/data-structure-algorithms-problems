def capitalletter(s):
	if len(s)==1:
		if ord(s[0])>=ord('A') and ord(s[0])<=ord('Z'):
			return s[0]
		return 'not found'
	if ord(s[0])>=ord('A') and ord(s[0])<=ord('Z'):
		return s[0]
	return capitalletter(s[1:])

print(capitalletter('taghJhs'))