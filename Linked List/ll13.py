class Node:
	def __init__(self, x):
		self.data=x
		self.next=None
		self.prev=None

class LL:
	def __init__(self, h):
		self.head=h 

	def cons_ll(self, arr):
		curr=self.head
		for i in arr:
			curr.next=Node(i)
			curr=curr.next

	def print_ll(self):
		curr=self.head
		while curr!=None:
			print(curr.data, end=' ')
			curr=curr.next


d={}
while curr!=None:
	if curr.data in d:
		d[curr.data]=d[curr.data]+1
	else:
		d[curr.data]=1
if d[curr.data]>1:
	print(curr.data)
	break