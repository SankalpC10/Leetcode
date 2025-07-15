class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            prevMap[crs].append(pre)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if prevMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            prevMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
