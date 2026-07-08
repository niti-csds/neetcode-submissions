class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        if x== 0:
            return 0
        elif x<=2:
            return 1
        
        r = x//2
        while l<=r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid  > x:
                r = mid-1
            else:
                l = mid+1
        return l-1
            
