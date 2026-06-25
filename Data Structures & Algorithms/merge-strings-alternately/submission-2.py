class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        m = len(word1)
        n = len(word2)

        if (m <= n):
            for i in range(m):
                res.append(word1[i])
                res.append(word2[i])
                
                
            for i in range(m,n):
                res.append(word2[i])
                

        else:
            for i in range(n):
                res.append(word1[i])
                res.append(word2[i])
                
                
            for i in range(n,m):
                res.append(word1[i])
        return "".join(res)
