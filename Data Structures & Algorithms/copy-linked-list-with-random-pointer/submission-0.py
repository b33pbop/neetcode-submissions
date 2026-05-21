"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a copy without node.random first
        ptr = head

        dummy = Node(0)
        cpy = dummy

        # maps original node to copied node
        node_map = {}

        while ptr:
            new_node = Node(ptr.val, ptr.next)
            cpy.next = new_node
            cpy = cpy.next

            node_map[ptr] = new_node
            ptr = ptr.next
        
        ptr = head
        cpy = dummy.next

        while ptr:
            random = ptr.random
            random_node = node_map.get(random, None)
            cpy.random = random_node

            ptr = ptr.next
            cpy = cpy.next

        return dummy.next        
