class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #for empty list
        if not nums:
            return 0
        left_p = 1
        
        for right_p in range(1,len(nums)) :
            if nums[right_p] != nums[right_p -1]:
                nums[left_p] = nums[right_p]
                left_p += 1
            
        return left_p

obj = Solution()
nums = [2,10,10,30,30,30]
print(obj.removeDuplicates(nums))
         