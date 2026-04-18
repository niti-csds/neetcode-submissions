class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #val : diff
        
        for ind, val in enumerate(nums):
            diff = target - val

            if diff in hashMap:
                return [hashMap[diff],ind]

            hashMap[val] = ind

            