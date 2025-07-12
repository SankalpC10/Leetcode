class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i] = float("inf")
            j=i
            for d,c in zip([1,7,30],costs):
                while j<n and days[j]<days[i]+d:
                    j+=1
                dp[i] = min(dp[i],c+dp[j])
        return dp[0]