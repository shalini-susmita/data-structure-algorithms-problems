class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

mini=float('-inf')
maxi=float('inf')

def check_BST(node, mini ,maxi):
  if node==None:
    return True
  if node.data<mini or node.data>maxi:
    return False
  return check_BST(node.left, mini, node.data-1) and check_BST(node.right, node.data+1, maxi)


def isBST(node):
  return check_BST(node, mini, maxi)


root=Node(12)
root.left=Node(8)
root.right=Node(14)
root.left.right=Node(90)

print(isBST(root))