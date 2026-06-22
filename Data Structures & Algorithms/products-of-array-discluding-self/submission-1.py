class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        pre = 1
        suff = 1
        for i in range(len(nums)-1):
            pre = pre * nums[i]
            prefix[i+1] = pre
        l = len(nums)-1
        while (l>0):
            suff = suff * nums[l]
            suffix[l-1] = suff
            l -= 1
        ans = [0]*len(nums)
        for i in range(len(ans)):
            ans[i] = prefix[i]*suffix[i]
        return ans


        


    