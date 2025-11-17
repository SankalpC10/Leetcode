class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_pos = -1
        cur = 0
        while cur<len(nums):
            if nums[cur] == 1:
                if  last_pos != -1 and cur-last_pos<=k:
                    return False
                last_pos = cur
            cur+=1
        return True