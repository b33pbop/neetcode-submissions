# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        ptr1 = list1
        ptr2 = list2

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = ptr2
                list2 = list2.next
                ptr2 = list2
            else:
                cur.next = ptr1
                list1 = list1.next
                ptr1 = list1
                
            cur = cur.next

        if list1 and not list2:
            cur.next = ptr1

        if list2 and not list1:
            cur.next = ptr2

        return dummy.next
