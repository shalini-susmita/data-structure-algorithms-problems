class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

x=[]
def inorder(node):
  if node==None:
    return 0
  inorder(node.left)
  x.append(node.data)
  inorder(node.right)

def kth_ele(node, k):
  inorder(node)
  return x[k-1]


root=Node(12)
root.left=Node(8)
root.right=Node(14)
root.left.right=Node(9)

print(kth_ele(root, 4))