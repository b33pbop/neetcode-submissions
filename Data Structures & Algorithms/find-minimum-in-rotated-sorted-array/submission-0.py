class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        nums = [4,5,6,7,0,1,2]
        mid = 7
        l = 4
        r = 2
        """
        l = 0
        r = len(nums) - 1
        smallest = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            smallest = min(smallest, nums[mid])

            # go left if the window is strictly increasing
            if nums[l] <= nums[r]:
                if nums[mid] <= nums[r]:
                    r = mid - 1
                elif nums[mid] >= nums[r]:
                    l = mid + 1
            elif nums[l] >= nums[r]:
                if nums[mid] <= nums[r]:
                    r = mid - 1
                elif nums[mid] >= nums[r]:
                    l = mid + 1

        return smallest
