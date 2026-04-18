class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch

        n = len(result)
        i = 0
        j = n - 1

        while i < j:
            if result[i] != result[j]:
                return False
            i += 1
            j -= 1

        return True