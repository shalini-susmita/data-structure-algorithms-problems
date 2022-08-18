def pangram(s):
	alpha='abcdefghijklmnopqrstuvwxyz'
	alpha1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	x='pangram'
	for i in range(len(alpha)):
		if alpha1[i] not in s and alpha[i] not in s: 
			x='not pangranm'
	
	return x

print(pangram('i am shalini susmita'))
print(pangram('We promptly judged antique ivory buckles for the next prize'))