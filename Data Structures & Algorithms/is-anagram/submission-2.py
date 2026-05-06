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
        
        count = set(freq.values())
        if 0 in count and len(count) == 1:
            return True
        
        return False