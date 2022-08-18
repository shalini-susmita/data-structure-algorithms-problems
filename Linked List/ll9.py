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

	def remove_dupli(self):
		curr=self.head
		while curr.next!=None:
			if curr.data==curr.next.data:
				new=curr.next.next
				curr.next=None
				curr.next=new
			else:
				curr=curr.next





arr=[1,2,2,2,3,5,5,8]
ll=LL(Node(arr[0]))
ll.cons_ll(arr[1:])
ll.print_ll()
print()
ll.remove_dupli()
ll.print_ll()