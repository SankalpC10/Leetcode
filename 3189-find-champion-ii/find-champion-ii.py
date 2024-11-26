class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = [0]*n
        for edge in edges:
            indegrees[edge[1]] += 1
        champ = -1
        champ_count = 0

        for i in range(n):
            if indegrees[i] == 0:
                champ_count += 1
                champ= i
        return champ if champ_count==1 else -1