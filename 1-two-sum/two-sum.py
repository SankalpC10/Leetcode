class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in hashmap:
                return [hashmap[req],i]
            hashmap[nums[i]] = i
        return []