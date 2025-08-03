class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m = len(heights),len(heights[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        #Initializing effort greed
        effort = [[float('inf')]*m for _ in range(n)]
        effort[0][0] = 0
        heap = [(0,0,0)] #(effort,row,col)

        while heap:
            curr_eff, r,c = heapq.heappop(heap)
            if r==n-1 and c==m-1:
                return curr_eff

            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<m:
                    next_eff = max(curr_eff,abs(heights[r][c] - heights[nr][nc]))
                    if next_eff<effort[nr][nc]:
                        effort[nr][nc] = next_eff
                        heapq.heappush(heap,(next_eff,nr,nc))
