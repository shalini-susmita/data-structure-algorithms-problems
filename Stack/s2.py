class queue:
	def __init__(self):
		self.s1=[]
		self.s2=[]

	def enqueu(self, x):
		while len(self.s1)!=0:
			self.s2.append(self.s1[-1])
			self.s1.pop()
		self.s1.append(x)

		while len(s2.self)!=0:
			self.s1.append(self.s2[-1])
			self.s2.pop()

	def dequeue(self):
		if len(self.s1)==0:
			print('empty')
		x=self.s1[-1]
		self.s1.pop()
		return x
