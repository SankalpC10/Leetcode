class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin,start = [0,0],[0,0]
        directionMap = {'U':[0,-1],'D':[0,1],'L':[-1,0],'R':[1,0]}
        for move in moves:
            start[0]+=directionMap[move][0]
            start[1]+=directionMap[move][1]
        return start==origin