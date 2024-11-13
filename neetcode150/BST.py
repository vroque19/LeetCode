class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class BST:
  def __init__(self, root=None):
    self.root = root
  
  def insert(self, val):
    print(f"adding {val}")
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

  def remove(self, node):
    if self.root is None:
      print("This tree is already empty")
    else:
      print(f"removing {node}...")
      self.root = self.remove_helper(self.root, node)

  def remove_helper(self, node, val):
    if node is None:
        print(f"{val} not found...")
        return None

    if val > node.val:
        node.right = self.remove_helper(node.right, val)
    elif val < node.val:
        node.left = self.remove_helper(node.left, val)
    else:
      if node.right is None and node.left is None:  # no children
          return None
      elif node.right is None:  # left child
          return node.left
      elif node.left is None:  # right child
          return node.right
      else:  # two children
          # Find the minimum node in the right subtree
          min_node = self.find_min(node.right)
          # Replace the current node's value with the minimum node's value
          node.val = min_node.val
          # Remove the minimum node from its original position
          node.right = self.remove_helper(node.right, min_node.val)
    return node
    
  def find_min(self, node):
      curr = node
      while curr and curr.left:
        curr = curr.left
      return curr
    

    
def main():
  tree = BST()
  
  tree.insert(2)
  tree.insert(5)
  tree.insert(10)
  tree.insert(1)
  tree.insert(6)
  tree.insert(7)


  print("in order traversal: ")
  tree.in_order_traverse(tree.root)
  print()
  tree.remove(1)
  print("in order traversal: ")
  tree.in_order_traverse(tree.root)

if __name__ == "__main__":
  main()
  
  