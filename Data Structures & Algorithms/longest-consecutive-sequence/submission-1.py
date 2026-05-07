class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # figure out start of sequence candidates first
        if len(nums) == 0:
            return 0

        set_nums = set(nums)
        sos = set()
        longest = 1

        for num in set_nums:
            if num - 1 not in set_nums:
                sos.add(num)
        
        for num in sos:
            length = 1
            while True:
                if num + 1 in set_nums:
                    length += 1
                    num += 1
                    set_nums.remove(num)
                else:
                    break
            longest = length if length > longest else longest
            length = 1

        return longest
                
