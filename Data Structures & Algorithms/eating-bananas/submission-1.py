class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h == len(piles):
            k = max(piles)
            return k
        l = 1
        k = 0
        r = max(piles)
        while(l < r):
            m = (l+r)//2
            hours = 0

            for n in piles:
                hours += (n + m-1)//m

            if hours <= h:
                r = m
            else:
                l = m+1
        return l
            
