class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if first > prices[i]:
                first = prices[i]
            else:
                profit = max(profit, prices[i] - first)
        return profit
                
            