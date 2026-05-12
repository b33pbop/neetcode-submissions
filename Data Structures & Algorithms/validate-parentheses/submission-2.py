class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for i in range(len(s)):
            if s[i] in table:
                stack.append(s[i])
                continue
            
            if not stack:
                return False
            else:
                cur = stack.pop()
                if table[cur] != s[i]:
                    return False
        
        return len(stack) == 0
