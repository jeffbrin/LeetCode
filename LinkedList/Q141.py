# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while fast is not None and slow is not fast:
            slow = slow.next
            fast = fast.next
            try:
                fast = fast.next
            except AttributeError:
                return False

        return fast is not None
