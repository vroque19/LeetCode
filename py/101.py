# https://leetcode.com/problems/symmetric-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        lvr_list = []
        rvl_list = []
        self.lvr(root.left, lvr_list)
        self.rvl(root.right, rvl_list)

        if lvr_list == rvl_list:
            return True
        return False

    def lvr(self, node, lst, dir='A'):
        if node is None:
            return
        self.lvr(node.left, lst, 'A')
        lst.append(str(node.val) + dir)
        self.lvr(node.right, lst, 'B')

    def rvl(self, node, lst, dir='A'):
        if node is None:
            return
        self.rvl(node.right, lst, 'A')
        lst.append(str(node.val) + dir)
        self.rvl(node.left, lst, 'B')
        