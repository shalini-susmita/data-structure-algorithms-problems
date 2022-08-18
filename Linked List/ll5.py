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

	def middle_node(self):
		curr=self.head
		i=0
		x=0
		j=1
		while curr!=None:
			curr=curr.next
			i=i+1
		
		x=((i+1)//2)
		curr=self.head
		while j!=x:
			j=j+1
			curr=curr.next
		print(curr.data)
		
	def middle_Node(self):
		curr=self.head
		i=1
		mid=self.head
		while currr!=None:
			curr=curr.next
			i=i+1
			if i%2!=0:
				mid=mid.next

		print(mid)

arr=[1,2,5,8,9,12,15,16,18,21,90]
x=LL(Node(arr[0]))
x.cons_ll(arr[1:])
x.print_ll()
print()
x.middle_node()