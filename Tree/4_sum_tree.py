class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x

arr=[0]
def store_inorder(root):
	if root==None:
		return
	store_inorder(root.left)
	arr.append(root.data)
	store_inorder(root.right)
	
def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)

def update_nodes(root):
	if root==None:
		return
	update_nodes(root.left)
	root.data=d[root.data]
	update_nodes(root.right)
	

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)

store_inorder(root)
arr.append(0)

d={}
x=[]

for i in range(1, len(arr)-1):
	x.append(arr[i-1]+arr[i+1])

for i in range(len(arr)-2):
	d[arr[i+1]]=x[i]

print('before updation')
inorder(root)
print()
update_nodes(root)
print('after updation')
inorder(root)
