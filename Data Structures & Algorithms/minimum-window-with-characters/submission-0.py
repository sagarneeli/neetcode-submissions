class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}
        for ch in t:
            count_t[ch] = 1 + count_t.get(ch, 0)

        have, need = 0, len(count_t)
        result = [-1, -1]
        length = float("inf")
        L = 0

        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)
            
            if s[R] in count_t and window[s[R]] == count_t[s[R]]:
                have += 1
            
            while have == need:
                if (R - L + 1) < length:
                    result = [L, R]
                    length = R - L + 1
                
                window[s[L]] -= 1
                if s[L] in count_t and window[s[L]] < count_t[s[L]]:
                    have -= 1
                
                L += 1
            
        L, R = result
        return s[L : R + 1] if length != float("inf") else ""
        