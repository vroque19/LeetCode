# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        slow = head
        fast = head.next
        found = False
        while not found:
            if fast.next is None or fast.next.next is None:
                found = True
            else:
                slow = slow.next
                fast = fast.next.next
        return slow.next
        


