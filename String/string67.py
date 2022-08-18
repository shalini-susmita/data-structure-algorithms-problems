def last_word(s):
	if s==' ':
		return 0
	x=s.split()
	c=len(x[-1])
	return c
	










print(last_word('Hello world    '))
print(last_word(' '))
print(last_word('Hello'))
print(last_word('i am shalini susmita'))
