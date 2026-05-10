class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        """
        AAABBBAB, k=1 -> replace A to get AAABBBBB
        A: 4
        B: 4
        window: AAA
        A: 1
        B: 4
        window: AAAB(A) -> store this as max window = 4
        A: 1
        B: 4
        window: BBB
        A: 1
        B: 1
        window: BBBA(B)
        A: 1
        B: 1
        window: BBBA(B)B -> max is now 5
        A: 1
        B: 0
        """
        max_freq = 0
        l = 0
        r = 0
        map = {}        

        while r < len(s):
            map[s[r]] = map.get(s[r], 0) + 1
            max_freq = max(max_freq, map[s[r]])
            r += 1 

            if max_freq + k < r - l:
                map[s[l]] -= 1
                l += 1

        return r - l
