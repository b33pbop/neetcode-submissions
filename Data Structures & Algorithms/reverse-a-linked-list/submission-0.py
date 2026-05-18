# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 3 pointers -> l, curr, r
        l = None
        curr = head

        while curr:
            r = curr.next
            curr.next = l
            l = curr
            curr = r

        return l
