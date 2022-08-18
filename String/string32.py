def repeat(s):
	x=s.split()
	z=[]
	for i in x:
		if i in z:
			return i
		else:
			z.append(i)









print(repeat('i am shalini am i a good shalini'))
print(repeat('i am shalini i am a good shalini'))
print(repeat('i am shalini shalini i a good am'))