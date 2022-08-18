class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

def insert_node(node, ele):
  newNode=Node(ele)
  x=root
  y=None
  while x!=None:
    y=x
    if ele<x.data:
      x=x.left
    else:
      x=x.right
  if y==None:
    y=newNode

  elif ele<y.data:
    y.left=newNode
  else:
    y.right=newNode
  return y

