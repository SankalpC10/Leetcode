class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M,N = len(obstacleGrid),len(obstacleGrid[0])
        dp = [0]*(N+1)
        dp[N-1] = 1
        for r in range(M-1,-1,-1):
            for c in range(N-1,-1,-1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                else:
                    dp[c]+=dp[c+1]
        return dp[0]