class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def diagonal(root):
	if root==None:
		return
	q=[]
	q.append(root)
	q.append(None)
	while len(q)>0:
		temp=q.pop(0)
		if not temp:
			if len(q)==0:
				return
			print(' ')
			q.append(None)
		else:
			while temp:
				print(temp.data, end=' ')
				if temp.left:
					q.append(temp.left)
				temp=temp.right

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)

diagonal(root)