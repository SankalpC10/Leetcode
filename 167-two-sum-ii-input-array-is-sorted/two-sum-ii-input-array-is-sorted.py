class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            req = target - numbers[i]
            if req in hashmap:
                return [hashmap[req],i+1]
            else:
                hashmap[numbers[i]] = i+1
        return -1