class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n1 = len(word1)
        n2 = len(word2)
        m = min(n1,n2)
        for i in range(m):
            res.append(word1[i])
            res.append(word2[i])
        if n2 > n1:
            res.extend(word2[n1:n2])
        
        elif n2 < n1:
            res.extend(word1[n2:n1])
        
        return "".join(res)


