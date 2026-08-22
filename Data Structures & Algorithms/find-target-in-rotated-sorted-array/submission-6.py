class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            r -= 1
        l_1 = r+1
        r_1 = len(nums) - 1

        if target < nums[l]:
            while(l_1<=r_1):
                m_1 = (l_1+r_1)//2
                if nums[m_1] == target:
                    return m_1
                elif nums[m_1] > target:
                    r_1 = m_1-1
                else:
                    l_1 = m_1+1
        else:
            while(l<=r):
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m]> target:
                    r = m-1
                else:
                    l = m+1
        return -1
                    

                    