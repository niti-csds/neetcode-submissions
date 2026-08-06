class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            ans = defaultdict(list)
            for word in strs:
                count = [0]*26
                for ch in word:
                    count[ord(ch)-ord('a')]+=1
                ans[tuple(count)].append(word) 
            #ans[(0,0,1).append(word)]
            return list(ans.values())
            #since the output is list so we are trying to convert       #dictionary to list and storing its values using .values()