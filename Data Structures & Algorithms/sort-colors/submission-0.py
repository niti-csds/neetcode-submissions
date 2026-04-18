class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        insert = 0
        for i in range(len(nums)):
            v = nums[i]
            count[v] += 1

        for i in range(len(count)):
            for j in range(count[i]):
                nums[insert] = i
                insert += 1
        return nums

obj = Solution()
nums = [2,1,0]
print(obj.sortColors(nums))      