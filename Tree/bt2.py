class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key

def level_order_trav(root):
	 q=[root]
	 while q!=[]:
	 	x=q.pop(0)
	 	print(x.data, end=' ')
	 	if x.left:
	 		q.append(x.left)
	 	if x.right:
	 		q.append(x.right)


root=Node(1)
root.left=Node(2)
root.right=Node(6)
root.left.right=Node(5)
root.left.right.left=Node(4)
root.left.right.left.right=Node(7)

level_order_trav(root)
