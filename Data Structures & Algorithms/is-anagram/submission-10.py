class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HashMap = [0]*28
        if len(s)!= len(t):
            return False
        for char in s:
            idx = ord(char) - ord('a')
            HashMap[idx]+=1
            
        for char in t:
            idx = ord(char) - ord('a')
            HashMap[idx]-=1
        for num in HashMap:
            if num > 0:
                return False
        return True