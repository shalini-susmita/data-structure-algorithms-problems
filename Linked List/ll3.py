class Node:
	def __init__(self, x):
		self.data=x
		self.next=None
		self.prev=None

class linked_list:
	def __init__(self, h):
		self.head=h11	

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

	def construct_rev_ll(self, arr):
		curr=self.head
		while curr.next!=None:
			curr.next.prev=curr
			curr=curr.next

	def print_rev(self):
		curr=self.head
		curr.prev=None
		while curr.next!=None:
			curr=curr.next
		while curr!=None:
			print(curr.data, end=' ')
			curr=curr.prev

arr=[1,2,3,4,5,6]
x=linked_list(Node(arr[0]))
x.cons_ll(arr[1:])
x.print_ll()
print()
x.construct_rev_ll(arr)
x.print_rev()