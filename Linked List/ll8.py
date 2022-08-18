class Node:
	def __init__(self, x):
		self.data=x
		self.next=None

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


arr1=[4,7,9,12,14]
arr2=[6,8,12,14]
ll1=LL(Node(arr1[0]))
ll2=LL(Node(arr2[0]))
ll1.cons_ll(arr1[1:])
ll2.cons_ll(arr2[1:])

curr1=ll1.head
curr2=ll2.head
d={}
while curr1!=None:
	if curr1.data in d:
		d[curr1.data]=d[curr1.data]+1
		
	else:
		d[curr1.data]=1
	curr1=curr1.next

while curr2!=None:
	if curr2.data in d:
		print(curr2.data)
		break
	else:
		curr2=curr2.next
