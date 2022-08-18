def first():
	second()
	print('this is first')

def second():
	third()
	print('this is second')

def third():
	fourth()
	print('this is third')

def fourth():
	print('this is fourth')

first()

