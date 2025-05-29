class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L,res,cur_sum = 0,0,0
        for R in range(len(arr)):
            cur_sum +=arr[R]
            if R-L+1 <k:
                continue
            if cur_sum/k >=threshold:
                res += 1
            cur_sum -=arr[L]
            L += 1
        return res            

