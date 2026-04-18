# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []
        for right in range(n):
            left = right - 1
            while left >=0 and pairs[left+1].key < pairs[left].key :
                #swap
                pairs[left],pairs[left+1] = pairs[left+1],pairs[left]
                left -= 1
            res.append(pairs[:])
        return res