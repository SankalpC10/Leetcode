class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval:interval[1])
        count = 0
        end_time = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= end_time:
                end_time = end
            else:
                count += 1
        return count
