def capitals(l):
	if len(l)==1:
		if ord(l[0][0])>=ord('A') or ord(l[0][0])<=ord('Z'):
			return(l[0])
		return(chr(ord(l[0][0])-32))







print(capitals(['dOg']))
# print(capitals(['dOg','bat','ABH']))
