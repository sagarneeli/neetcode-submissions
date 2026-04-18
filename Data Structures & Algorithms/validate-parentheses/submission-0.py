class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for ch in s:
            if ch in char_map.values():
                stack.append(ch)
                continue

            if stack and stack[-1] == char_map[ch]:
                stack.pop()
            else:
                return False
        
        return not stack
        