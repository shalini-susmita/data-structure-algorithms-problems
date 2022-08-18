students={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
height=float(input('enter height'))
weight=int(input('enter weight'))
for i in students:
	if students[i][0]>height and students[i][1]>weight:
		print(i, students[i])