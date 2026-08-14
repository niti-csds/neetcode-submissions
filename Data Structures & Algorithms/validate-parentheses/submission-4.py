class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{': '}', '[': ']', '(': ')'}
        stack = []

        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif not stack:
                return False
            elif pairs[stack.pop()] != ch:
                return False

        return len(stack) == 0