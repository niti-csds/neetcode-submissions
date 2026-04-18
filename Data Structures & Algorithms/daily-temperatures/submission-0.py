class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = [] #[temp,ind]
        
        for i,t in enumerate(temperatures):
            while stack and t >  stack[-1][0]:
                #value of top element:
                stackT,index = stack.pop()
                res[index] = i-index
            stack.append((t,i))
        return res




            