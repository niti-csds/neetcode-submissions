class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # horizonta,vertical
        max_a = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind,val = stack.pop()
                start = ind
                max_a = max(max_a,(i - ind)*val )

            stack.append((start,h))
        for i,h in stack:
            max_a = max(max_a, h*(len(heights) - i))
        return max_a
        