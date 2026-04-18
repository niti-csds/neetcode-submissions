class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_p = 0
        for right_p in range(len(nums)):
            if nums[right_p] != val:
                nums[left_p] = nums[right_p]
                left_p += 1
        return left_p
        
obj = Solution()
nums = [1,1,2,3,4]
print(obj.removeElement(nums, 1))