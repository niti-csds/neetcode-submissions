class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr_dict = defaultdict(int)
        res = []
        for n in nums:
            arr_dict[n] += 1
        
        while (k>0):
            max_ = 0
            for key, values in arr_dict.items():
                if values >= max_:
                    max_ = values
                    k_ = key
            
            res.append(k_)
            arr_dict.pop(k_)
                    

            k -= 1

        return res
