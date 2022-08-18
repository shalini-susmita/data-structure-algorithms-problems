def reverse(n):
	if len(n)==1:
		print(n[0], end='')
		return
	
	reverse(n[1:])
	print(n[0], end='')


reverse('shalini')