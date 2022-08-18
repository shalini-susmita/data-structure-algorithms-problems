student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]

s={}
for i in range(len(student_id)):
	s[student_id[i]]={student_name[i]:student_grade[i]}

print(s)