class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashmap method
        map = {}
        longest = 0

        # maps num : length of sequence starting with num
        for num in nums:
            if num not in map:
                prev = 0 if (num - 1) not in map else map[num - 1]
                next = 0 if (num + 1) not in map else map[num + 1]
                map[num] = prev + next + 1
                map[num - prev] = map[num]
                map[num + next] = map[num]
                longest = max(longest, map[num])
        return longest
