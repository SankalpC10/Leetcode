class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p,lowest = 0,prices[0]
        for i in prices:
            max_p = max(i-lowest, max_p)
            lowest = min(lowest, i)
        return max_p
