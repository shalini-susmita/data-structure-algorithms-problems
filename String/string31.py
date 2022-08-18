def vowels(s):
	vowel='aeiouAEIOU'
	v=0
	for i in s:
		if i in vowel:
			print(i, end=' ')
			v=v+1
	print(v)






vowels('w3resource')