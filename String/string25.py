def specified(a,b):
	
		if b[:len(a)]==a:
			return True
		else:
			return False
		



print(specified('abhi', 'abhishek'))
print(specified('abhi', 'shalini'))