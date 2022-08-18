num={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

num_z={}
for i in num:
	num_z[num[i]]=0

print("num_z is ", num_z)

for i in num:
	print("Incrementing value of key ", num[i], " by 1, now numz[", num[i], "] is ", num_z[num[i]]+1)
	num_z[num[i]]=num_z[num[i]]+1
	



print(num_z)