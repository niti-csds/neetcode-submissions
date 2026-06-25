class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        max_sub = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                res+=nums[i]
            else:
                res = nums[i]
            max_sub = max(res,max_sub)
        return max_sub