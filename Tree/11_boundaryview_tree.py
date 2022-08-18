class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def printLeaves(root):
	if not root:
		return
	printLeaves(root.left)
	printLeaves(root.right)
	if root.left==None and root.right==None:
		print(root.data, end=' ')

def leftboundary(root):
	if root==None:
		return
	if root.left:
		print(root.data, end=' ')
		leftboundary(root.left)
	elif root.right:
		print(root.data, end=' ')
		leftboundary(root.right)	


def rightboundary(root):
	if root==None:
		return
	if root.right:
		rightboundary(root.right)
		print(root.data,end=' ')
	elif root.left:
		rightboundary(root.left)
		print(root.data,end=' ')

def printBoundary(root):
	if root==None:
		return 
	print(root.data, end=' ')
	leftboundary(root.left)
	printLeaves(root)
	rightboundary(root.right)



root=Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.right.right=Node(5)


printBoundary(root)