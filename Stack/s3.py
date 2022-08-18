class stack:
	def __init(self):
		self.q1=[]
		self.q2=[]

	def push(self, x):
		self.q2.append(x)
		while len(self.q1)!=0:
			self.q2.append(self.q1[0])
			self.q1.pop()

	def pop(self):
		while len(self.q1)!=0:
			self.q1.pop(-1)
