alpha='my name is @shalini'

alpha_dict={}
for i in range(97,123):
	
	alpha_dict[chr(i)]=0

for i in alpha:
	if ord(i)>=97 and ord(i)<=123:
		alpha_dict[i]=alpha_dict[i]+1

for i in alpha_dict:
	print(i, alpha_dict[i])

