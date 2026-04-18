class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max = nums[0]
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]

        arr = [0]*(max+1)
        s_index = 1
        if max <= 0:
            return 1
        for n in nums:
            if n >=0:
                arr[n] += 1
            
        while s_index < len(arr):
            if arr[s_index] == 0:
                return s_index
            s_index += 1
        return s_index

            

