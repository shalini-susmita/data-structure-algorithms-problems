class Node:
	def __init__(self, x):
		self.data=x
		self.next=None

arr=[1,0,8,0,2,3]
head=Node(arr[0])
curr=head
for i in arr[1:]:
	curr.next=Node(i)
	curr=curr.next

curr=head
prev=None
while curr!=None:
	if curr.data==0:
		prev.next=curr.next
		curr.next=head
		head=curr
		curr=prev.next
	else:
		prev=curr
		curr=curr.next

curr=head
while curr!=None:
	print(curr.data, end=' ')
	curr=curr.next





