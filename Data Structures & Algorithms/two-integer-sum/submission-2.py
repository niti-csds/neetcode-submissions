class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
                d[nums[i]] = i
        for i,val in enumerate(nums):
            req = target - val
            if req in d and i!= d[req]:
                return [min(i,d[req]),max(i,d[req])]
             
        