# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        print(first, "\n")
        for _ in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
            print(dummy, "\n")
        # loop stops right before the nth node from the end
        second.next = second.next.next # skips the nth node

        return dummy.next

