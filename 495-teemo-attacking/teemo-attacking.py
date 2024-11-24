class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        n = len(timeSeries)
        poison_time = 0
        for i in range(n-1):
            poison_duration = min(duration,timeSeries[i+1]- timeSeries[i])
            poison_time += poison_duration
        poison_time += duration
        return poison_time