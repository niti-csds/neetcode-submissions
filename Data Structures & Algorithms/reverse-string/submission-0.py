class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            temp = s[left]
            s[left]= s[right]
            s[right] = temp
            right -= 1
            left += 1
        return s

