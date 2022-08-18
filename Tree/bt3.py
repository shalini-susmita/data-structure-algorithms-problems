class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key

def identical_trees(node1,node2):
	if node1==None and node2==None:
		return True
	if node1 and node2:
		if node1.data==node2.data:
			return identical_trees(node1.left, node2.left) and identical_trees(node1.right, node2.right)
	return False



root=Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.right.right=Node(5)

root2=Node(1)
root2.left=Node(2)
root2.right=Node(4)
root2.left.left=Node(2)
root2.right.right=Node(5)

print(identical_trees(root, root2))
