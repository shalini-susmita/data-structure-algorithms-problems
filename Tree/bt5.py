class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key

def depth(node):
	if node==None:
		return 0
	return 1+max(depth(node.left), depth(node.right))



root=Node(1)
root.left=Node(2)
root.right=Node(6)
root.left.right=Node(5)
root.left.right.left=Node(4)
root.left.right.left.right=Node(7)


root=Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.right.right=Node(5)

print(depth(root))