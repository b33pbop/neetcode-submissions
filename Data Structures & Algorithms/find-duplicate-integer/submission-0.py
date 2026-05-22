class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat nums like a linked list where each val is an index
        # [1, 3, 4, 2, 2] -> idx 0 -> idx 1 -> idx 3 -> idx 2 -> idx 4 -> idx 2 -> idx 4 ... (cycle)

        # floyd's algorithm suggests that distance from idx 0 to start of cycle
        # is the same as the distance between the point where slow and fast pointer meets
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        dst_ptr = 0
        while True:
            slow = nums[slow]
            dst_ptr = nums[dst_ptr]
            if slow == dst_ptr:
                return slow

        
