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



root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)



def insert(x):

	q=[root]
	while len(q)!=0:
		t=q.pop(0)
		if t.left==None:
			t.left=Node(x)
			break
		else:
			q.append(t.left)
		if t.right==None:
			t.right=Node(x)
			break
		else:
			q.append(t.right)

insert(10)
inorder(root)


