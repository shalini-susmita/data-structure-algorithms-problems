class Cylinder:
	def __init__(self):
		self.x=[]

	def pop(self):
		self.x.pop(-1)

	def push(self, q):
		self.x.append(q)

	def elements(self):
		return self.x

	def top(self):
		return self.x[-1]


stack1=Cylinder()
stack2=Cylinder()
stack3=Cylinder()

_=input()
u=list(map(int, input().split()))
r=list(map(int, input().split()))
w=list(map(int, input().split()))

for i in u:
	stack1.push(i)
for i in r:
	stack2.push(i)
for i in w:
	stack3.push(i)

sum_equal=False
while len(stack1.elements())>0 and len(stack2.elements())>0 and len(stack3.elements())>0:
	sum1=sum(stack1.elements())
	sum2=sum(stack2.elements())
	sum3=sum(stack3.elements())

	s=min(sum1,min(sum2,sum3))

	while sum1>s:
		sum1=sum1-stack1.top()
		stack1.pop()
	while sum2>s:
		sum2=sum2-stack2.top()
		stack2.pop()
	while sum3>s:
		sum3=sum3-stack3.top()
		stack3.pop()
	if sum1==sum2==sum3:
		sum_equal=True
		break

if sum_equal:
	print(s)
else:
	print(0)



























# 	s1=sum(h1)
# 	s2=sum(h2)
# 	s3=sum(h3)
# 	while h1 and h2 and h3:
# 		m=min(s1,s2,s3)

# 		while s1>m:
# 			pop(h1[0])
# 			s1-=h[0]
# 		while s2>m:
# 			pop(h2[0])
# 			s2-=h2[0]
# 		while s3>m:
# 			pop(h3[0])
# 			s3-=h[0]
# 		if s1==s2==s3:
# 			return m 
# 	return 0

# cyl=Cylinder()
# print()
