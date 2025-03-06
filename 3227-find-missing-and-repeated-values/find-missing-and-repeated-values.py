class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n= len(grid)
        count_dict = {i:0 for i in range(1,((n)**2)+1)}
        for i in range(n):
            for j in range(n):
                element = grid[i][j]
                count_dict[element]+=1
        res = [-1,-1]
        for k,v in count_dict.items():
            if v==0:
                res[1] = k
            elif v==2:
                res[0] = k
        return res
