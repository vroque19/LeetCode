# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])

        while queue:
            curr_level_size = len(queue)
            max_val = float('-inf')

            for _ in range(curr_level_size):
                curr = queue.popleft()
                # queue.pop()
                max_val = max(max_val, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(max_val)

        root.left = None
        root.right = None
        return res
        
