class Node:
	def __init__(self, key):
		self.left=None
		self.right=None
		self.data=key

def inorder(root):
	inorder(root.left)
	print(root.data)
	inorder(root.right)



root=Node(1)
root.left=Node(2)