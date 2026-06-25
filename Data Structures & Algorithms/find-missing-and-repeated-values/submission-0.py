class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        do = 0
        m = 0
        flat = [num for row in grid for num in row]
        set_nums = set(flat)

        hashmap = defaultdict(int)
        for i in range(len(flat)):
            hashmap[flat[i]]+=1
            
        
        for num in range(1,len(flat)+1):
            if hashmap[num] > 1:
                do = num
            elif hashmap[num] == 0:
                m = num
            
                
        return [do,m]


