class Node:
	def __init__(self, x):
		self.data=x
		self.next= None

class linked_list:
	def __init__(self, h):
		self.head=h

	def link_list_construct(self, arr):
		curr=self.head
		for i in arr:
			curr.next=Node(i)
			curr=curr.next

	def print_linked_list(self):
		curr=self.head
		while curr!=None:
			print(curr.data, end=' ')
			curr=curr.next

	def end_node_addition(self, ele):
		x=Node(ele)
		curr=self.head
		while curr.next!=None:
			curr=curr.next
		curr.next=x

	def front_node_add(self, ele):
		x=Node(ele)
		x.next=self.head
		self.head=x

	def in_between(self,ele,prev_node):
		x=Node(ele)
		curr=self.head
		while curr.data!=prev_node.data:
			curr=curr.next
		x.next=curr.next
		curr.next=x
	
	def delete_node(self, ele):
		x=Node(ele)
		curr=self.head
		prev=None
		while curr.data!=ele:
			prev=curr
			curr=curr.next
		prev.next=curr.next

	def delete_front(self):
		self.head=self.head.next
	


arr=[1,2,3,4,5]
x=linked_list(Node(arr[0]))
x.link_list_construct(arr[1:])
x.print_linked_list()
# x.end_node_addition(6)
# x.print_linked_list()
# x.front_node_add(80)
# x.print_linked_list()
print()
x.in_between(71, Node(3))
x.print_linked_list()
print()
x.delete_node(4)
x.print_linked_list()
print()
x.delete_front()
x.print_linked_list()
	
