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

	def printNode_from_last(self, n):
		main=self.head
		ref=self.head
		count=0
		
		while count!=n:
			count=count+1
			ref=ref.next
		while ref!=None:
			ref=ref.next
			main=main.next
		print(main.data)
		

arr=[1,2,3,4,5,6]
ll=LL(Node(arr[0]))
ll.cons_ll(arr[1:])
ll.print_ll()
print()
ll.printNode_from_last(5)

