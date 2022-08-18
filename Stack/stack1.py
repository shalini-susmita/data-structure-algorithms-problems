class MaxStack:
	def __init__(self):
		self.liss=[]

	def push(self, x):
		self.liss.append(x)

	def pop(self):
		if len(self.liss)>=1:
			self.liss.pop(-1)
		else:
			print('Trying to pop from empty stack')

	def maxi(self):
		if len(self.liss)>=1:
			return sorted(self.liss)[-1]
		return 'Stack empty'


stackmax=MaxStack()

x=int(input())
for i in range(x):
	y=list(map(int, input().split()))
	if len(y)==2:
		stackmax.push(y[1])	
	else:
		if y[0]==2:
			stackmax.pop()
		else:
			print(stackmax.maxi())


