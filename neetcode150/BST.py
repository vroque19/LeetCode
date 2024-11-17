import icecream as ic
from collections import deque

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
    
    
  def isBalanced(self, root)->bool:
    return self.balancedHelper(root)[0] # are all the subtrees balanced?
  
  def balancedHelper(self, node) -> list:
     if node is None:
        return [True, 0]
     bal = False
     l = self.balancedHelper(node.left)
     r = self.balancedHelper(node.right)
     h = 1 + max(l[1], r[1])
     if abs(l[1] - r[1]) <=1 and l[0] and r[0]:
        bal = True
     return [bal, h]
  
  def bfs(self, root):
    queue = deque()
    level = 0
    if root:
      queue.append(root)
    while len(queue) > 0:
      print("level: ", level)
      for i in range(len(queue)):
        curr = queue.popleft()
        print(curr.val)
        if curr.left:
          queue.append(curr.left)
        if curr.right:
          queue.append(curr.right)
      level += 1

  
     
    # if root is None:
    #    return True
    # left = self.getHeight(root.left)
    # right = self.getHeight(root.right)
    # if abs(left-right) > 1:
    #    return False
    # # call isBalanced on the left and right subtrees
    # return self.isBalanced(root.left) and self.isBalanced(root.right)
  
  def getHeight(self, node) -> int:
     if node is None:
        return 0
     return max(self.getHeight(node.left) + 1, self.getHeight(node.right)+1)
    
def main():
  tree = BST()
  
  tree.insert(3)
  tree.insert(1)
  tree.insert(5)
  tree.insert(8)
  tree.insert(9)
  tree.insert(4)
  


  print("in order traversal: ")
  tree.in_order_traverse(tree.root)
  print()
  # tree.remove(1)
  print("in order traversal: ")
  tree.in_order_traverse(tree.root)
  print("height: ", tree.getHeight(tree.root))
  print(tree.isBalanced(tree.root))
  tree.bfs(tree.root)

if __name__ == "__main__":
  main()
  
  