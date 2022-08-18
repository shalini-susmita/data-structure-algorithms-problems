class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def insert(root, key):
	if root==None:
		return Node(key)
	else:
		if root.data==key:
			return root
		elif key<=root.data:
			if root.left==None:
				root.left=Node(key)
			else:
				insert(root.left, key)
		else:
			if root.right==None:
				root.right=Node(key)
			else:
				insert(root.right, key)


def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


root=Node(70)
root.left=Node(50)
root.right=Node(90)
root.left.left=Node(30)
root.right.right=Node(100)
root.left.left.left=Node(20)
root.right.left=Node(80)
root.right.left.right=Node(85)

inorder(root)
insert(root, 99)
print()
inorder(root)
