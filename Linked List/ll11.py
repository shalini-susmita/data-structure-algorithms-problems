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


	def end_node(self, x):
		curr=self.head
		prev=None
		i=1
		while curr.next!=None:
			curr=curr.next
		while curr!=None:
			if i!=x:
				i=i+1
				curr=curr.prev
			else:
				return curr.data
				

			

arr=[1,2,3,4,5]
ll=LL(Node(arr[0]))
ll.cons_ll(arr[1:])
ll.print_ll()
print()
ll.construct_rev_ll(arr)
ll.print_rev()
print()
print(ll.end_node(3))