class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        case 1: strictly increasing
        nums = [1,3], target = 3
        l = 0, r = 1
        mid = 0

        case 2: rotated
        nums = [4,5,6,7,0,1,2], target = 5
        nums = [4,5,6,0,1,2,3], target = 4
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
