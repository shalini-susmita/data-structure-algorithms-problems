class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x
		self.hd=1000000

def bottomview(root):
	if root==None:
		return
	hd=0
	m={}
	q=[]
	root.hd = hd
	q.append(root)

	while len(q)!=0:
		temp=q[0]
		q.pop(0)
		hd=temp.hd
		m[hd] = temp.data

		if temp.left!=None:
			temp.left.hd = hd-1
			q.append(temp.left)

		if temp.right!=None:
			temp.right.hd = hd+1
			q.append(temp.right)

	for i in sorted(m.keys()):
		print(m[i], end=' ')


root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)


bottomview(root)