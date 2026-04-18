class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = []
        n = 2*len(nums)
        right_p = 0
        for left_p in range(n):
            if right_p == len(nums):
                right_p = 0
            new.append(nums[right_p])
            right_p += 1
        return new
obj = Solution()
nums = [22,21,20,1]
print(obj.getConcatenation(nums))