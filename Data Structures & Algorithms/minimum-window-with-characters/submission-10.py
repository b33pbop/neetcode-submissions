class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        map_t = {}
        window = {}

        # populate target map
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1

        l = 0
        criteria = len(map_t)   # number of unique chars still unmet

        best_len = float('inf')
        best_start = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            # fulfilled one character requirement
            if s[r] in map_t and window[s[r]] == map_t[s[r]]:
                criteria -= 1

            # try to shrink the window will all characters in t is in the window
            while criteria == 0:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_start = l

                # remove left char
                window[s[l]] -= 1

                # if removing breaks requirement
                if s[l] in map_t and window[s[l]] < map_t[s[l]]:
                    criteria += 1

                l += 1

        if best_len == float('inf'):
            return ""

        return s[best_start:best_start + best_len]
