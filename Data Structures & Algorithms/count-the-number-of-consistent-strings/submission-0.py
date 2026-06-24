class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_w = set(allowed)
        for s in words:
            consist = True

            for ch in s:
                if ch not in allowed_w:
                    consist = False
                    break
                
            if consist:
                count+=1 
        return count