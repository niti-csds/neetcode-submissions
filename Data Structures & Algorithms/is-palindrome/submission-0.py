class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        st = "".join(s)
        r = len(st)-1
        while(l<=r):
            while l<r and  not st[l].isalnum():
                l += 1
            while r>l and not st[r].isalnum():
                r -= 1
            if st[l].lower() != st[r].lower():
                    return False
            l += 1
            r -= 1
        return True