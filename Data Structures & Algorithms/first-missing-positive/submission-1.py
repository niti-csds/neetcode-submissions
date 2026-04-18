class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if max(nums)<=0:
            return 1
        find = 1
        i = 0
        while i < len(nums):
            if nums[i] == find:
                find += 1
                i = 0
            else:
                if i == len(nums):
                    return find
                i += 1
        return find
            
