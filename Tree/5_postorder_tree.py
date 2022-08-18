class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def postorder(root):
	if root==None:
		return
	s1=[]
	s2=[]
	s1.append(root)
	while s1:
		node=s1.pop()
		s2.append(node)
		if node.left:
			s1.append(node.left)
		if node.right:
			s1.append(node.right)

	while s2:
		node=s2.pop()
		print(node.data, end=' ')


root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)


postorder(root)