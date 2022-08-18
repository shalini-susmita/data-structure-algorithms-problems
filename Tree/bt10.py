class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

def leftview(node):
  q=[root]
  res=[]
  while q!=[]:
    y=[]
    for i in range(len(q)):
      x=q.pop(0)
      y.append(x.data)
      if x.left:
        q.append(x.left)
      if x.right:
        q.append(x.right)
    res.append(y[0])
  print(res)

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)


leftview(root)
