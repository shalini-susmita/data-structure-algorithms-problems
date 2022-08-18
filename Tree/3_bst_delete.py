class Node:
	def __init__(self, x):
		self.left= None
		self.right= None
		self.data= x



def minValue(root):
	while root.left!=None:
		riit=root.left
	return root


def delete(root, key):
	if root==None:
		return root
	if key<root.data:
		root.left=delete(root.left, key)
	elif key>root.data:
		root.right=delete(root.right, key)
	else:
		if root.left==None and root.right==None:
			return None
		else:
			if root.left==None:
				root.data=root.right.data
				root.right=None

			elif root.right==None:
				root.data=root.left.data
				root.left=None
			else:
				temp=minValue(root.right)
				root.data=temp.data
				root.right=delete(root.right, temp.data)
	return root

def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


root=Node(70)
root.left=Node(50)
root.right=Node(90)
root.left.left=Node(30)
root.right.right=Node(100)
root.left.left.left=Node(20)
root.right.left=Node(80)
root.right.left.right=Node(85)


inorder(root)
delete(root, 90)
print()
inorder(root)



