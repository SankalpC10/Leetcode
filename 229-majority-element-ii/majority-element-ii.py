class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap,res = {},[]
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        for k,v in hashmap.items():
            if v>len(nums)/3:
                res.append(k)
        return res