# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # [1, 2, 3, 4, 5, 6] -> [1, 6, 2, 5, 3, 4]
        # half 1: [1, 2, 3], half 2: [4, 5, 6] (reverse this half)
        # 1 -> 2 -> 3 -> 6 -> 5 -> 4 (pointer on 1 and 6 then merge from there)

        # find mid point first
        slow = head
        fast = head

        # slow will stop at the mid point (starting node of the second half)
        # 1, 2, 3, 4, 5, 6
        # ^        ^
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            fast = curr.next
            curr.next = prev
            prev = curr
            curr = fast

        # 1, 2, 3, 4 | 6, 5
        # ^            ^

        first = head
        second = prev
        
        while second:
            first_ptr = first.next
            second_ptr = second.next

            first.next = second
            second.next = first_ptr

            first = first_ptr
            second = second_ptr
