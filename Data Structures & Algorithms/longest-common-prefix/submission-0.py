class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs,key=len)
        for word in strs:
            i =0 
            while i <len(prefix) and prefix[i]== word[i]:
                i+=1
            prefix = prefix[:i]
            if prefix == "":
                return ""
        return prefix



