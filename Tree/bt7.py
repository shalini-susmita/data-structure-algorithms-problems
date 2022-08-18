class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key


def mirror(node):
  if node==None:
    return 0
  else:
    temp=node
    mirror(node.left)
    mirror(node.right)
    temp=node.left
    node.left=node.right
    node.right=temp


def inorder(node):
  if node==None:
    return 0
  inorder(node.left)
  print(node.data, end=' ')
  inorder(node.right)


root=Node(1)
root.left=Node(2)
root.right=Node(6)
root.left.right=Node(5)
root.left.right.left=Node(4)
root.left.right.left.right=Node(7)

inorder(root)
print()
mirror(root)
inorder(root)