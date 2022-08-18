class Stock:
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

stock1=Stock()
stock2=Stock()

x=list(map(int, input().split()))

y=[]
for i in x:
	T=1
	while stock1.is_empty()==False and i>=stock1.top():
		stock2.push(stock1.top())
		stock1.pop()
		T=T+1
	while stock2.is_empty()==False:
		stock1.push(stock2.top())
		stock2.pop()
	
	stock1.push(i)
	y.append(T)

print(y)