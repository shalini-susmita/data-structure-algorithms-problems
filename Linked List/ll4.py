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

	def Node_place(self, k):
		curr=self.head
		i=1
		while i!=k:
			i=i+1
			curr=curr.next
		print(curr.data)



arr=[1,2,5,8,9,12,15]
x=LL(Node(arr[0]))
x.cons_ll(arr[1:])
x.print_ll()
print()
x.Node_place(1)