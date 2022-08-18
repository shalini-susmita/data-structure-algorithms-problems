class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x
		self.hd=0

def topview(root):
	if root==None:
		return 
	hd=0
	m={}
	q=[]
	root.hd=hd
	q.append(root)

	while len(q)!=0:
		temp=q[0]
		q.pop(0)
		current_hd=temp.hd

		if current_hd not in m:
			m[current_hd]=temp.data
		if temp.left:
			temp.left.hd=current_hd-1
			q.append(temp.left)
		if temp.right:
			temp.right.hd=current_hd+1
			q.append(temp.right)

	for i in m.keys():
		print(m[i],end=' ')


root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)


topview(root)
