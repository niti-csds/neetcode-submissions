class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        long = 0
        
        for num in numsSet:
            if num-1 in numsSet:
                continue
            else:
                count = 1
                while num+count in numsSet:
                    count += 1
                long = max(long,count)
        return long

