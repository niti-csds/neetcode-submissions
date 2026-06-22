class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        
        res = "".join(c.lower() for c in s if c.isalnum())
        r = len(res)-1
        while(l<=r):
            if(res[l] != res[r]):
                return False
            l+=1
            r-=1
        return True


            