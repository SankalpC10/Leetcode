class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        
        min_heap = []
        for num,freq in counts.items():
            heapq.heappush(min_heap,[freq,num])
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        res = []
        for freq,num in min_heap:
            res.append(num)
        return res
