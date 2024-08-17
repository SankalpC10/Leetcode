class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, low = 0,prices[0]
        for i in prices:
            max_profit = max(i-low, max_profit)
            low  = min(i, low)
        return max_profit
