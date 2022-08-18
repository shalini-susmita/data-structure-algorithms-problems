class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key

def height(node):
	if node==None:
		return 0
	return 1+max(height(node.left), height(node.right))

def diameter(node):
	if node==None:
		return 0
	return max(max(diameter(node.left), diameter(node.right)), height(node.left)+ height(node.right)+1)


root=Node(1)
root.left=Node(2)
root.right=Node(6)
root.left.right=Node(5)
root.left.right.left=Node(4)
root.left.right.left.right=Node(7)

print(diameter(root))