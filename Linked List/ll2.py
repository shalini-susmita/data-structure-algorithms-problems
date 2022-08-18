class Node:
	def __init__(self, x):
		self.data=x
		self.next=None

class linked_list:
	def __init__(self, h):
		self.head=h
	def construct_ll(self, arr):
		curr=self.head
		for i in arr:
			curr.next=Node(i)
			curr=curr.next
			
	def print_ll(self):
		curr=self.head
		while curr!=None:
			print(curr.data, end=' ')
			curr=curr.next
	def ele_sorted_arr(self, ele):
		x=Node(ele)
		prev=None
		curr=self.head
		while curr!=None and ele>curr.data:
			prev=curr
			curr=curr.next
		if prev==None:
			self.head=x
			return
		if curr==None:
			prev.next=x
			x.next=None
			return
		x.next=curr
		prev.next=x

arr=[11,12,15,17,18]
ll=linked_list(Node(arr[0]))
ll.construct_ll(arr[1:])
ll.print_ll()
print()
ll.ele_sorted_arr(60)
ll.print_ll()