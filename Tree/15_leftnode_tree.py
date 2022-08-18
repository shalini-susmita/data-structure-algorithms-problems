class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def updatetree(root):
	if root==None:
		return 0
	if root.left==None and root.right==None:
		return root.data

	ls=updatetree(root.left)
	rs=updatetree(root.right)

	root.data=root.data+ls 
	return root.data+rs

def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.left.right= Node(5)
root.right.right= Node(6)


print(updatetree(root))
inorder(root)