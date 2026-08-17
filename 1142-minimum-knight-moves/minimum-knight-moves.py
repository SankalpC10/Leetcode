class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
        q = deque([(0,0,0)])
        visited = {(0,0)}
        while q:
            cx,cy,moves = q.popleft()
            if(cx,cy) == (x,y):
                return moves
            for dx,dy in directions:
                nx,ny = cx+dx, cy+dy
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny,moves+1))
        return -1