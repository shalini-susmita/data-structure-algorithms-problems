class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x


def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


def depth_deletion(root, d_node):
	q=[root]
	while len(q)!=0:
		t=q.pop(0)
		if t.left==d_node:
			t.left=None
			return
		if t.right==d_node:
			t.right=None
			return 
		if t.left!=None:
			q.append(t.left)
		if t.right!=None:
			q.append(t.right)


def deletion(root, d):
	q=[root]
	while len(q)!=0:
		t=q.pop(0)
		if t.data==d:
			x=t
		if t.left!=None:
			q.append(t.left)
		if t.right!=None:
			q.append(t.right)
	x.data=t.data
	depth_deletion(root, t)




root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)


inorder(root)
print()
deletion(root, 4)
inorder(root)



