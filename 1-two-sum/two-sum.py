class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in hashmap:
                return [hashmap[req],i] 
            else:
                hashmap[nums[i]] = i
        return [0]