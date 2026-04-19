class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]*len(prices)
        max_profit = 0
        for i in range(len(prices)-1):
            j = i+1
            profit[i] = prices[j]-prices[i] 
        for i in range(len(profit)):
            if profit[i] > 0:
                max_profit += profit[i]
                
        return max_profit

