class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def search(root, key):
	if root.data==key:
		print('found')
	if key<root.data:
		if not root.left:
			print('not found')
			return
		if root.left.data==key:
			print('Found')
		else:
			search(root.left, key)
	else:
		if not root.right:
			print('Not found')
			return
		if root.right.data==key:
			print('Found')
		else:
			search(root.right, key)
	


root=Node(70)
root.left=Node(50)
root.right=Node(90)
root.left.left=Node(30)
root.right.right=Node(100)
root.left.left.left=Node(20)
root.right.left=Node(80)
root.right.left.right=Node(85)

search(root, 5)