class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_dist  = 0
        for i in range(1,len(arrays)):
            max_dist  = max(max_dist, abs(arrays[i][-1]-smallest), abs(biggest - arrays[i][0]))
            smallest  = min(smallest, arrays[i][0])
            biggest = max(biggest, arrays[i][-1])
        return max_dist
            
                    