class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                cur = num
                length = 1

                while cur + 1 in set_nums:
                    cur += 1
                    length += 1

                longest = max(longest, length)

        return longest
                
