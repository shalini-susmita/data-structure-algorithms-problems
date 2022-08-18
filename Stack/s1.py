class Node:
	def __init__(self, x):
		self.data=x
		self.next=None
		self.prev=None

class LinkedList:
	def __init(self, h):
		self.head=h
			
	def cons_ll(self, arr):
		curr=self.head
		for i in arr:
			curr.next=Node(i)
			curr=curr.next

	def print_ll(self):
		curr=self.head
		while curr.next!=None:
			print(curr.data, end=' ')
			curr=curr.next

	def push_end(self, ele):
		ele_node=Node(ele)
		curr=self.head
		while curr.next!=None:
			curr=curr.next
		curr.next=ele_node

	def pop_end(self):
		curr=self.head
		prev=None
		while curr.next!=None:
			prev=curr
			curr=curr.next
		prev.next=None

	def top_node(self):
		curr=self.head
		while curr.next!=None:
			curr=curr.next
		print(curr.data)

	def isEmpty(self):
		if self.head==None:
			return True
		return False

	def size_ll(self):
		x=0
		curr=self.head
		while curr.next!=None:
			x=x+1
			curr=curr.next
		return x


class stack:
	def __init__(self, obj):
		self.ll_obj = obj

	def push(self, ele):
		self.ll_obj.push_end(ele)

	def pop(self):
		self.ll.pop_end()

	def is_empty(self):
		return self.ll.is_empty()

	def top(self):
		self.ll.top_node()


ll = LinkedList()
stk = stack(ll)
stk.push(3)