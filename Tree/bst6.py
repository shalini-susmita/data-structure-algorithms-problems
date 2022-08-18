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

def sumz(node, k):
  inorder(node)
  print(x)
  start=0
  end=len(x)-1
  while start!=end:
    if k>sum([x[start], x[end]]):
      start=start+1
      print(start)

    elif k<sum([x[start], x[end]]):
      end=end-1
    elif k==sum([x[start], x[end]]):
      return True
  return False

root=Node(12)
root.left=Node(8)
root.right=Node(14)
root.left.right=Node(9)

print(sumz(root, 23))