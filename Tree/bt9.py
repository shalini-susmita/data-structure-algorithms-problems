class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

def zigzag(node):
  Flag=True
  res=[]
  q=[root]

  while q!=[]:
    ans=[]
    for i in range(len(q)):
      
      x=q.pop(0)
      ans.append(x.data)
      if x.left:
        q.append(x.left)
      if x.right:
        q.append(x.right)
    if Flag!=True: 
      ans=list(reversed(ans))
    Flag=not Flag
    res=[*res, *ans] 
  print(res)

def inorder(node):
  if node==None:
    return 0
  inorder(node.left)
  print(node.data, end=' ')
  inorder(node.right)

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)

inorder(root)
print()
zigzag(root)
