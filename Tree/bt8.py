class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.data=key

def height(node):
  if node==None:
    return 0
  return 1+max(height(node.left), height(node.right))

def isBalanced(node):
  if node==None:
    return 0
  else:
    isBalanced(node.left)
    isBalanced(node.right)
    if abs(height(node.left)- height(node.right)) <=1:
      return True
    return False


root=Node(1)
root.left=Node(2)
root.right=Node(6)
root.left.right=Node(5)
root.left.right.left=Node(4)
root.left.right.left.right=Node(7)

root=Node(1)
root.left= Node(2)
root.right = Node(3)
root.left.left= Node(4)
root.right.left= Node(6)
root.right.right= Node(7)
root.right.left.left= Node(8)
root.right.right.right= Node(9)

print(isBalanced(root))