class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            #lests see integer hai ya exp
            if n in ['+','-','*','/']:
                if len(stack)>=2 :
                    a = stack[-1]
                    b = stack[-2]
                    stack.pop()
                    stack.pop()
                    if n == '+':
                        exp = int(a+b)
                    elif n == '-':
                        exp = int(b-a)
                    elif n == '*':
                        exp = int(b*a)
                    elif n=='/':
                        exp = int(b/a)
                    
                    stack.append(exp)
            else:
                stack.append(int(n))
        return stack[-1] 
