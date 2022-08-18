class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def leftview(root, level, max_level):
	if root==None:
		return 	
	if max_level[0]<level:
		print(root.data, end=' ')
		max_level[0]=level 

	leftview(root.right, level+1, max_level)
	leftview(root.left, level+1, max_level)


def leftView(root):
	max_level=[0]
	leftview(root, 1, max_level)

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)


leftView(root)