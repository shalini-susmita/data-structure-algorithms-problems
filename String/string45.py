def camel_case(s):
	a=0
	for i in s:
		if i>='A' and i<='Z':
			a=a+1
	if s=='':
		return a
	return a+1



print(camel_case('abhiShaliniSusmitaShailyGoldy'))
print(camel_case(''))