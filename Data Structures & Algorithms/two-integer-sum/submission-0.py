class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    indices.append(i)
                    indices.append(j)
                    break

        return indices

obj = Solution()
nums = [3,4,5,6]
target = 7
print(obj.twoSum(nums,target))