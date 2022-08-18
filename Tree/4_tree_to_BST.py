class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

def inorderList(root, store):
	if root==None:
		return 0
	inorderList(root.left, store)
	store.append(root.data)
	inorderList(root.right, store)

def storeToBST(store, root):
	if root==None:
		return 0
	storeToBST(store, root.left)
	root.data=store[0]
	store.pop(0)
	storeToBST(store, root.right)

def treeToBST(root):
	if root==None:
		return
	arr=[]
	inorderList(root, arr)
	arr.sort()
	storeToBST(arr, root)

def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)

root=Node(10)
root.left=Node(30)
root.right=Node(15)
root.left.left=Node(20)
root.right.right=Node(5)

inorder(root)
treeToBST(root)
print()
inorder(root)	

