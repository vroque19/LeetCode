# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        res = []
        def inOrder(root):
            if not root:
                return
            res.append(root.val)
            inOrder(root.right)
            inOrder(root.left)
        inOrder(root)
        freq_table = collections.Counter(res)
        mode = max(freq_table.values())
        return [ x for x in freq_table if freq_table[x] == mode]
