class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for number in nums:
            hashmap[number]+=1
        top_k = list(sorted(hashmap.values(), reverse = True))[:k]
        req = []
        for k,v in hashmap.items():
            if v in top_k:
                req.append(k)
        return req
        

        