# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        # remove first node if n == size of linked list
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        tmp = slow.next.next
        slow.next = tmp

        return head
