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

	def is_paliandrome(self):
		curr=self.head
		i=0
		j=0
		k=0
		while curr.next!=None:
			i=i+1
			curr=curr.next
		x=((i+1)//2)
		end=curr
		curr1=self.head
		while k!=x:
			if curr1.data!=end.data:
				return False
				
			else:
				curr1=curr1.next
				end=end.prev
				k=k+1
		return True





arr=[1,2,3,2,1]
ll=LL(Node(arr[0]))
ll.cons_ll(arr[1:])
ll.print_ll()
print()
ll.construct_rev_ll(arr)
ll.print_rev()
print()
print(ll.is_paliandrome())

