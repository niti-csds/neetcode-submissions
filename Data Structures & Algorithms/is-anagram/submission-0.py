class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in s:
            d1[c] += 1
        for c in t:
            d2[c] += 1
        
        for ch in s:
            if d1[ch] != d2[ch]:
                return False
        return True

        