class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class BST:
  def __init__(self, root=None):
    self.root = root
  
  def insert(self, val):
    if self.root is None:
      self.root = Node(val)
    else:
      self.insert_helper(self.root, val)
    
  def insert_helper(self, node, val):
    if node is None:
      return Node(val)
    if val > node.val:
      node.right = self.insert_helper(node.right, val)
    elif val < node.val:
      node.left = self.insert_helper(node.left, val)
    return node # return current node after insertion

  def in_order_traverse(self, node):
    if node:
      self.in_order_traverse(node.left)
      print(node.val, end=" ")
      self.in_order_traverse(node.right)

    
def main():
  tree = BST()
  
  tree.insert(2)
  tree.insert(5)
  tree.insert(10)
  tree.insert(1)
  tree.insert(6)
  print("in order traversal: ")
  tree.in_order_traverse(tree.root)
  print()

if __name__ == "__main__":
  main()
  
  