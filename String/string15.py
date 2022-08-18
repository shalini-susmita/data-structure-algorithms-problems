def add_ing_ly(s):
	if len(s)>2:
		if s[-3:]=='ing':
			s=s+'ly'

		else:
			s+'ing'

		
	return s


print(add_ing_ly('shalini'))
print(add_ing_ly('ping'))
print(add_ing_ly('sy'))