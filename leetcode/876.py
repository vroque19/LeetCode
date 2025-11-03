# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trailing, leading = head, head.next
        if leading is None:
            return trailing
        while leading.next:
            trailing = trailing.next
            leading = leading.next.next
            if leading is None:
                return trailing
        return trailing.next

        
