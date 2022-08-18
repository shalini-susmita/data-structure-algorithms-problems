class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def mirror(root):
	q=[root]
	while len(q):
		curr=q[0]
		q.pop(0)
		curr.left , curr.right= curr.right, curr.left

		if curr.left:
			q.append(curr.left)
		if curr.right:
			q.append(curr.right)

def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data,end=' ')
	inorder(root.right)

root=Node(1)
root.left= Node(10)
root.right = Node(3)
root.left.left= Node(4)
root.left.right= Node(6)
root.right.right= Node(31)

inorder(root)
mirror(root)
print()
inorder(root)
