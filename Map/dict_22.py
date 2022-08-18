colors=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

s={}
for i in colors:
	s[i[0]]=[]

for i in colors:
	s[i[0]].append(i[1])

print(s)

