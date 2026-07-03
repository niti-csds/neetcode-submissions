class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        ans = 0
        for c in operations:
            if c != '+' and c != 'D' and c != 'C':
                res.append(int(c))
            
            elif c == '+':
                prev = int(res.pop())
                prevv = int(res.pop())
                res.append(prevv)
                res.append(prev)
                res.append(prev+prevv)

            elif c == 'D':
                prev = int(res.pop())
                res.append(prev)
                res.append(2*prev)
            else:
                prev = res.pop()
        for r in res:
            ans += r
        return ans
                

            