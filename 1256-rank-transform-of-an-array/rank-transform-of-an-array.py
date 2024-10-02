class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap = {}
        nums = sorted(set(arr))
        rank = 1
        for num in nums:
            hashmap[num] = rank
            rank +=1
        for i in range(len(arr)):
            arr[i] = hashmap[arr[i]]
        return arr
