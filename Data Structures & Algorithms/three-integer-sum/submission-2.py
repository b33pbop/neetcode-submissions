class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort first
        # [-4, -1, -1, 0, 1, 2]
        # -nums[i] == nums[j] + nums[k]

        # use 2 pointer approach to find nums[j] + nums[k] with target = -nums[i]
        nums.sort()
        result = set()

        for i in range(0, len(nums) - 2):
            target = -nums[i]

            j = i + 1
            k = len(nums) - 1

            while j < k and j > i:
                if nums[j] + nums[k] == target:
                    result.add(tuple((nums[i], nums[j], nums[k])))
                    j += 1
                    k -= 1

                elif nums[j] + nums[k] < target:
                    j += 1

                elif nums[j] + nums[k] > target:
                    k -= 1
        
        result = list(result)
        for triplet in result:
            triplet = list(triplet)

        return result
