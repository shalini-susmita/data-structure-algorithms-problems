def TOH(n, _from, to, via):
	if n==0:
		return
	TOH(n-1, 'A', 'B', 'C')
	print('Shift disc', n, 'from', _from, 'to', to)
	TOH(n-1, 'B', 'C', 'A')

TOH(5, 'A', 'C', 'B')