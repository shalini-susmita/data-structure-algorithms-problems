class Node:
	def __init__(self, x):
		self.data= x
		self.next= None               

class linkedlist:
	def __init__(self):
		self.head= None

	def push_at_front(self, data):

		# create a node
		node=Node(data)
		# point the next of this node to linkedlist's head
		node.next=self.head
		# make this node linkedlist's head
		self.head=node

	def push_at_back(self, data):
		node=Node(data)
		x=self.head
		while x.next!=None:
			x=x.next
		x.next=node

	def push_in_between(self, data, prev_node):
		node=Node(data)
		node.next=prev_node.next
		prev_node.next=node

	def display(self):
		x=self.head
		while x!=None:
			print(x.data, end=' ')
			x=x.next

	def delete(self, data):
		curr_node=self.head
		prev_node=None
		while curr_node.data!=data:
			prev_node=curr_node
			curr_node=curr_node.next
		prev_node.next=curr_node.next





# ll=linkedlist()
# node=Node(5)
# ll.head=node
# ll.push_at_back(6)
# ll.push_at_back(7)
# ll.push_at_back(8)
# ll.push_at_back(9)

# ll.display()

liss=['My', 'name', 'is', 'SS']

ll=linkedlist()

ll.head=Node(liss[0])
for i in liss[1:]:
	ll.push_at_back(i)

ll.display()
print()
ll.delete(liss[1])
ll.display()








