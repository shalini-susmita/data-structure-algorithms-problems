class Number:
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

stack1=Number()
stack2=Number()

x=list(map(int, input().split()))

y=[]
for i in reversed(x):

	while stack1.is_empty()==False and stack1.top()<i:
		stack2.push(stack1.top())
		stack1.pop()
	if stack1.is_empty()==False:
		y.append(stack1.top())
	else:
		y.append(-1)
	while stack2.is_empty==False:
		stack1.push(stack2.top())
		stack2.pop()
	stack1.push(i)
			

print(list(reversed(y)))

