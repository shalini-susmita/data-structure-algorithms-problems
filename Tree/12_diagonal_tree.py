class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def diagonal(root):
	if root==None:
		return
	node=root
	q=[]
	LQ=[]
	while node:
		q.append(node.data)
		
		if node.left:
			LQ.append(node.left)
		if node.right:
			node=node.right
		else:
			if len(LQ)>=1:
				node=LQ.pop(0)
			else:
				node=None
	return q

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)

print(diagonal(root))