class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def sum(root):
	if root==None:
		return 0
	return (sum(root.left) + root.data + sum(root.right))

def isSumtree(root):
	if root==None:
		return True
	if root.left==None and root.right==None:
		return True
	if root.data==sum(root.left)+sum(root.right) and isSumtree(root.left) and isSumtree(root.right):
		return True
	return False

root=Node(26)
root.left= Node(10)
root.right = Node(3)
root.left.left= Node(4)
root.left.right= Node(6)
root.right.right= Node(3)


print(isSumtree(root))