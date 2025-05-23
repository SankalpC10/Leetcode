class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit,lowest_ever = 0,prices[0]
        for i in range(len(prices)):
            max_profit = max(max_profit,prices[i]-lowest_ever)
            lowest_ever = min(lowest_ever,prices[i])
        return max_profit