class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        compare = (len(nums)//2)
        arr = [0]*(max(nums)+1)
        for i in range(len(nums)):
            indexOfarr = nums[i]
            arr[indexOfarr] += 1
        return arr.index(max(arr))
            
