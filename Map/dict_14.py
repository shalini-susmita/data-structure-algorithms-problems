class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]

s={}

for i in range(len(class_list)):
	s[class_list[i]]=id_list[i]
	
print(s)