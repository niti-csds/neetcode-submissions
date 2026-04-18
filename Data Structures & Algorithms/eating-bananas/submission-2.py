class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)
        k_min = 1
        while k_min <= k_max:
            mid = (k_max + k_min)//2
            hrs_ate = 0
            for i in range(len(piles)):
                if piles[i] <= mid:
                    hrs_ate += 1
                elif piles[i] % mid ==0:
                    hrs_ate += piles[i]//mid
                else :
                    hrs_ate += piles[i]//mid +1
            if hrs_ate <= h:
                #left half
                k = mid
                k_max = mid - 1
            else :
                k_min = mid + 1
        return k 

        

        

        

obj = Solution()
nums = [25,10,23,4]
print(obj.minEatingSpeed(nums,7))