class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        for num in arr:
            hashmap[num] = 1+hashmap.get(num,0)
        res = -1
        for k,v in hashmap.items():
            if k==v:
                res = max(res,k)
        return res