# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        ans = [0]
        def dfs(root):
            if root is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            ans[0] = max(ans[0], 2 + left + right)

            return 1 + max(left, right)
        dfs(root)
        return ans[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        