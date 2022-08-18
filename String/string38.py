def password(n, s):
	x=0
	numbers = "0123456789"
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_characters = "!@#$%^&*()-+"

	is_num=False
	is_lc=False
	is_uc=False
	is_sc=False

	for i in s:
		if i in numbers:
			is_num=True
		if i in lower_case:
			is_lc=True
		if i in upper_case:
			is_uc=True
		if i in special_characters:
			is_sc=True

	x=int(not is_num)+int(not is_lc)+int(not is_uc)+int(not is_sc)

	if (len(s)+x)<6:
		n=6-len(s)
	else:
		n=x

	return n

for l, v in [(2, '@1'), (2, '@@'), (1, '1'), (6, 'abc123')]:
	print(password(l, v))

