class Bracket:
	def __init__(self):
		self.x=[]

	def pop(self):
		self.x.pop(-1)

	def push(self, q):
		self.x.append(q)

	def is_empty(self):
		if len(self.x)==0:
			return True
		return False

	def top(self):
		return self.x[-1]

brac=Bracket()

_=int(input())
for i in _:
	p=input()

	d={'{':'}', '[':']', '(':')'}

	for i in p:
		if i in d.keys():
			brac.push(i)
		elif i in d.values():
			if d[brack.top()]==i:
				brac.pop()

	if brack.is_empty():
		print('Yes')
	else:
		print('No')














