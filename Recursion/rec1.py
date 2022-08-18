def recursive(n):
	if n<1:
		print('n is less than 1')
	else:
		recursive(n-1)
		print(n)

recursive(3)

# recursive(2)
# recursive(1)
# recursive(0)
# print('0 is less than 1')
# print(1)
# print(2)
# print(3)
