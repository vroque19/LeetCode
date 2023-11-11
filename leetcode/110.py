# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.checkBalance(root)
        return self.isBalanced

    def checkBalance(self, root):
        if root is None:
            return 0
        leftHeight = self.checkBalance(root.left)
        rightHeight = self.checkBalance(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.isBalanced = False

        return max(leftHeight, rightHeight) + 1 
        
        