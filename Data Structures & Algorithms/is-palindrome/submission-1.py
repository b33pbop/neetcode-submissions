class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use 2 pointers at the start and end
        # for each character, we check if isalnum then lower or upper it
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i <= j:
            front = s[i]
            back = s[j]

            if front.isalnum() and back.isalnum():

                if front != back:
                    return False

                i += 1
                j -= 1
            else:
                if not front.isalnum():
                    i += 1
                if not back.isalnum():
                    j -= 1
        
        return True
            