class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x


def inorder(root):
	curr=root
	stack=[]
	while True:

		while curr!=None:
			stack.append(curr)
			curr=curr.left
		if curr==None and stack!=[]:
			curr=stack.pop(-1)
			print(curr.data, end=' ')
			curr=curr.right
		else:
			break

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)

inorder(root)