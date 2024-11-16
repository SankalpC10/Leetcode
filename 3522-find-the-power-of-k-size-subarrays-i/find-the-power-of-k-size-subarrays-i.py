class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            q = []
            for j in range(i,i+k):
                if len(q)==0:
                    q.append(nums[j])
                elif nums[j]-q[-1] != 1:
                    break
                else:
                    q.append(nums[j])
            if len(q)==k:
                res.append(max(q))
            else:
                res.append(-1)
        return res

