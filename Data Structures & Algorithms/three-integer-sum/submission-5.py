class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort first
        # [-4, -1, -1, 0, 1, 2]
        # -nums[i] == nums[j] + nums[k]

        # use 2 pointer approach to find nums[j] + nums[k] with target = -nums[i]
        nums.sort()
        result = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1

                elif sum < 0:
                    j += 1

                elif sum > 0:
                    k -= 1

        return result
