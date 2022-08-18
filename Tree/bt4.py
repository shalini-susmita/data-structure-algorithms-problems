class Node:
	def __init__(self,key):
		self.left=None
		self.right=None
		self.data=key


def isSym(n1, n2):
	if n1==None and n2==None:
		return True
	if n1 and n2:
		if n1.data==n2.data:
			return isSym(n1.left, n2.right) and isSym(n1.right, n2.left)
	return False


root=Node(1)
root.left=Node(2)
root.right=Node(2)
root.left.left=Node(3)
root.right.right=Node(3)

print(isSym(root.left, root.right))