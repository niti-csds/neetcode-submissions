class Solution:
    def scoreOfString(self, s: str) -> int:
       
        score = 0
        for i in range(len(s)-1):
            if ord(s[i]) < ord(s[i+1]):
                score = score + (ord(s[i+1]) - ord(s[i]))
            else:
                score = score + (ord(s[i]) - ord(s[i+1]))

        return score


        
