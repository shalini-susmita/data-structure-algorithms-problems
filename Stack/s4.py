class Bracket:
	def __init__(self):
		self.x=[]

	def push(self, ele):
		self.x.append(ele)

	def pop(self):
		self.x.pop(len(self.x)-1)



s=Bracket()
q='{()}[]'
a=['{', '(', '[']
b=['}', ')', ']']
for i in q:
	if i in a:
		s.push(i)
	elif i in b:
		s.pop(i)

