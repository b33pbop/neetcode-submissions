class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        nums = [-1,0,2,4,6,8], target = 4
        
        mid = len(nums) // 2 -> 4

        if target == nums[mid]: return mid
        if target > nums[mid]: go right else go left
        """

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1
        
        return -1
        