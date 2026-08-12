class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dic = defaultdict(list)
        s = set(nums)

        for n in s:
            if n - 1 not in s:
                dic[n] = []

        res = []

        for key in dic:
            i = 1
            while key + i in s:
                dic[key].append(key + i)
                i += 1

            res.append(len(dic[key]) + 1)

        return max(res) if res else 0

