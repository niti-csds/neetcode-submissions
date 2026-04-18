class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        n = len(heights)-1
        j = n
        max = 0
        while i < j:
            b = j-i
            if heights[i] <= heights[j]:
                l = heights[i]
                i+=1
            else:
                l = heights[j]
                j-=1
            if max < l*b:
                max = l*b

        return max