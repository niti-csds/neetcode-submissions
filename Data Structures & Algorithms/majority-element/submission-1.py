class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num1 = -1
        cnt = 0
        for num in nums:
            if num1 == num:
                cnt += 1
            elif cnt == 0:
                num1 = num
            else :
                cnt -= 1
        return num1
        