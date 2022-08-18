def count(s):
	d={}
	for i in s:
		d[i]=0
	for i in s:
		d[i]=d[i]+1
		
	for i in d:
		if d[i]>1:
			print(i, d[i])


count('thequickbrownfoxjumpsoverthelazydog')