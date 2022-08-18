class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def printLevelOrder(root, level, ltr):
	if root==None:
		return
	if level==0:
		print(root.data, end=' ')
	elif level>0:
		if ltr:
			printLevelOrder(root.left, level-1, ltr)
			printLevelOrder(root.right, level-1, ltr)
		else:
			printLevelOrder(root.right, level-1, ltr)
			printLevelOrder(root.left, level-1, ltr)

def height(node):
	if node==None:
		return 0
	return 1 + max(height(node.left), height(node.right))

def printSpiral(root):
	h=height(root)
	ltr=True
	for i in range(0, h+1):
		printLevelOrder(root, i, ltr)
		print()
		ltr = not ltr

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)


printSpiral(root)


