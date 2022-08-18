
fac_list= [1,1]
for i in range(2, 11):
	fac_list.append(i * fac_list[i-1])


x=int(input())
print(fac_list)