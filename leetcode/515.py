# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # result list of max values at each lvl
        res = []
        # empty tree returns empty list
        if not root:
            return res
        queue = deque([root])

        while queue:
            curr_level_size = len(queue)
            max_val = float('-inf')

            for _ in range(curr_level_size):
                # FIFO dequeue the current node
                curr = queue.popleft()

                # update the maximum value
                max_val = max(max_val, curr.val)

                # enqueue the left and right children if they exist
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # add the max value of the value
            res.append(max_val)

        return res
        
