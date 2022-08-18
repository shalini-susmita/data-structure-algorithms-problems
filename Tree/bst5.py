class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

def lCA(node, k1, k2):
  if node==None:
    return None
  if node.data>k1 and node.data>k2:
    return lCA(node.left, k1, k2)
  if node.data<k1 and node.data<k2:
    return lCA(node.right, k1, k2)

  return node.data

root=Node(20)
root.left= Node(8)
root.right = Node(22)
root.left.left= Node(4)
root.left.right= Node(12)


print(lCA(root, 4, 12))