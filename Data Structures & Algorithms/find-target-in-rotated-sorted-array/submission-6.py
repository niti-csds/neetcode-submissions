class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                #mid is in left sorted portion
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                    r = mid-1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                else:
                    l = mid +1
                 
        return -1


             


