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
        
        for i in range(len(t)):
            if t[i] not in freq:
                return False
            
            if freq[t[i]] <= 0:
                return False

            freq[t[i]] -= 1
        
        return True