quantity=int(input('Enter quantity\n'))
total_amount=100*quantity
if total_amount>1000:
	discount=total_amount*10/100
	final_amount=total_amount-discount
	print(final_amount)
else:
	print(total_amount)
