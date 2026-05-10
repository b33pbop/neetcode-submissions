class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide window of size s1 across s2
        # use array of size 26 -> O(26) = O(1)

        freq_s1 = [0 for _ in range(26)]
        freq_s2 = [0 for _ in range(26)]
        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        l = 0
        r = 0

        for i in range(m):
            freq_s1[ord(s1[i]) - 97] += 1

        while r < n:
            while r - l + 1 <= m:
                freq_s2[ord(s2[r]) - 97] += 1
                r += 1
            
            if freq_s1 == freq_s2:
                return True
            
            freq_s2[ord(s2[l]) - 97] -= 1
            l += 1

        return False
        