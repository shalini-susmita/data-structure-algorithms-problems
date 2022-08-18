class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key
    self.parent=None


def minVal(node):
  curr=node
  while curr!=None:
    if curr.left==None:
      break
    curr=curr.left
  return curr.data

def successor(node):
  if node.right!=None:
    return minVal(node.right)
  while node.parent!=None:
    if node.data==node.parent.left.data:
      return node.parent.data



  




print(successor(root,3 ))
