class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(len(prices)-1):
            j = i+1
            if (prices[j]-prices[i]) > 0:
                max_profit +=  prices[j]-prices[i]
        
                
        return max_profit