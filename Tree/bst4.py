class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

l=[]
def inorder(node):
  if node==None:
    return 0
  inorder(node.left)
  l.append(node.data)
  inorder(node.right)
 


def delete(node, ele):
  if node==None:
    return 0
  if node.left.data==ele:
    if node.left.left or node.left.right:
      node.left=node.left.left 
      node.left=node.left.right

  if node.right.data==ele:
    if node.right.right or node.right.left:
      node.right=node.right.right
      node.right=node.right.left

  if node.left.data==ele:
    x=1[fvpdf=-]





