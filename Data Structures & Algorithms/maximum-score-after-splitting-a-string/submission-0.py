class Solution:
    def maxScore(self, s: str) -> int:
        one_l = 0
        l = 0
        z = 0
        o = 0
        max_s = 0
        for num in s:
            if num == '0':
                z+=1
            else:
                o+=1
        # z = 2 , o = 4 total = 6
        total = 6
        z_v = 0
        n = len(s)
        r = l+1
        while(r<n):
            if s[r-1] == '0':
                z_v += 1
                
            else:
                o-=1
            res = o+z_v
            r+=1
                
            max_s = max(max_s,res)
        return max_s







            
