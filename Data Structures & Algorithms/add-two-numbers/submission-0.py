# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 pass, track sum of each node and carry over
        carry = 0
        dummy = ListNode()
        cur = dummy

        while l1 or l2:
            if not l1:
                node_sum = l2.val + carry
                l2 = l2.next
            elif not l2:
                node_sum = l1.val + carry
                l1 = l1.next
            else:
                node_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            
            carry = node_sum // 10

            if carry == 1:
                node_sum = node_sum % 10
            
            cur.next = ListNode(node_sum, None)
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(1, None)

        return dummy.next
