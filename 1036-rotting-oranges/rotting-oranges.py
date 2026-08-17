class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        fresh = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        q = deque()
        time = 0
        ROWS,COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        while fresh >0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr, c+dc
                    if (0<=row<ROWS and 0<=col<COLS and grid[row][col]==1):
                        grid[row][col]=2
                        fresh -=1
                        q.append((row,col))
            time+=1
        return time if fresh==0 else -1
