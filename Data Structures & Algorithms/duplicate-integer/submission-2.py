class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for ptr in range(i+1,len(nums)):
                if nums[i] == nums[ptr]:
                    return True
                    break
        return False
obj = Solution()
nums = [1,2,3,3]
print(obj.hasDuplicate(nums))
            