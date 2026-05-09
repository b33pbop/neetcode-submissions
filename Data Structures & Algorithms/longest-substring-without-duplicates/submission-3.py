class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "advdf" -> [a, d, v]
        move start from a till d
        """
        # sliding window
        # use a set to check for duplicates
        substring_set = set()
        start = 0
        end = 0
        longest = 0

        while end < len(s):
            # move start to the first instance of the repeated character
            while s[end] in substring_set:
                substring_set.discard(s[start])
                start += 1
        
            substring_set.add(s[end])
            longest = max(longest, end - start + 1)
            end += 1
            
        return longest
