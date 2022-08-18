class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

def search_bst(node, ele):
  if node==None:
    return 'Null'
  elif node.data==ele:
    return node.data
  elif node.data>ele:
    return search_bst(node.left, ele)
  return search_bst(node.right, ele)

root=Node(12)
root.left=Node(8)
root.right=Node(14)
root.left.right=Node(9)


print(search_bst(root, 7))