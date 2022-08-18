class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

x=[]
def store_inorder(root):
	if root==None:
		return
	store_inorder(root.left)
	x.append(root.data)
	store_inorder(root.right)


def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)

def add_greater(x):
	i=len(x)-2
	y=[x[len(x)-1]]
	while i>=0:
		y.append(x[i]+y[len(x)-2-i])
		i=i-1
	return y

def update_tree_inorder(root, y):
	if root==None:
		return
	update_tree_inorder(root.left, y)
	root.data=y[0]
	y.pop(0)
	update_tree_inorder(root.right, y)

root=Node(5)
root.left=Node(2)
root.right=Node(13)

store_inorder(root)
a=add_greater(x)
a=list(reversed(a))
update_tree_inorder(root, a)
print()
inorder(root)



