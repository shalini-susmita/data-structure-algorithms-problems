item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

l=[]
for i in item_list:
	if i not in l:
		l.append(i)

print(l)

