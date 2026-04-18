class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        HashSet = set(nums)
        new_n = len(HashSet)

        if n > new_n:
            return True
        return False