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



arr1=[2,5,8]
arr2=[1,4,9]
ll1=LL(Node(arr1[0]))
ll2=LL(Node(arr2[0]))

ll1.cons_ll(arr1[1:])
ll2.cons_ll(arr2[1:])

if ll1.head.data<ll2.head.data:
	x=ll1.head.data
	curr1=ll1.head.next
	curr2=ll2.head
else:
	x=ll2.head.data
	curr2=ll2.head.next
	curr1=ll1.head
ll3=LL(Node(x))

curr3=ll3.head
while curr1!=None and curr2!=None:
	if curr1.data<curr2.data:
		curr3.next=curr1
		curr1=curr1.next
	else:
		curr3.next=curr2
		curr2=curr2.next
	curr3=curr3.next
if curr1==None:
	curr3.next=curr2
else:
	curr3.next=curr1



ll3.print_ll()
