class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}  #char-count
        if len(s) != len(t):
            return False
        for c in s:
            s_map[c] = 1 + s_map.get(c,0)

        for c in t:
            s_map[c] = s_map.get(c,0) - 1
            if s_map[c] == -1:
                return False

        for c , count in s_map.items():
            if s_map[c] != 0:
                return False
        
        return True
        