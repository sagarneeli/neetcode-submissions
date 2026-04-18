class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        length = 0
        char_map = defaultdict(int)

        for R in range(len(s)):
            char_map[s[R]] += 1

            while (R - L + 1) - max(char_map.values()) > k:
                char_map[s[L]] -= 1
                L += 1

            length = max(length, R - L + 1)
        
        return length
        