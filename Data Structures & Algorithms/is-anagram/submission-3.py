class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

            if t[i] in freq:
                freq[t[i]] -= 1
            else:
                freq[t[i]] = -1
        
        for j in freq.values():
            if j != 0:
                return False
        return True