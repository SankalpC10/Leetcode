class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0]*n
        stack = []
        for i in range(n):
            while stack and heights[i]>heights[stack[-1]]:
                idx = stack.pop()
                answer[idx]+=1
            if stack:
                answer[stack[-1]] += 1
            stack.append(i)
        return answer
