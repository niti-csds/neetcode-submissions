class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialize an empty set
        check = set()
        for num in nums:
            if num in check:
                return True
            check.add(num)
        return False
obj = Solution()
nums = [1,2,3,3]
print(obj.hasDuplicate(nums))