class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'{':'}','[':']','(':')'}
        res = []
        if len(s)%2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                res.append(s[i])
            elif not res:
                return False
            else:
                if res:
                    p = res[-1]
                    if dict[p] != s[i]:
                        return False
                    else:
                        res.pop()
                    
                    
        if not res:
            return True
        else:
            return False
 
        
