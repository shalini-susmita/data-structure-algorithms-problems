class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def printLeft(root):
	if root==None:
		return
	q=[]
	q.append(root)
	while len(q):
		x=len(q)
		for i in range(0, x):
			temp=q[0]
			q.pop(0)
			if i==0:
				print(temp.data, end=' ')
			if temp.left:
				q.append(temp.left)
			if temp.right:
				q.append(temp.right)

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)

printLeft(root)