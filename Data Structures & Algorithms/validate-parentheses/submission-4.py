class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for c in s:
            if c in table:
                stack.append(c)
                continue
            
            if not stack:
                return False
            
            cur = stack.pop()
            if table[cur] != c:
                return False
        
        return len(stack) == 0
