class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        for start,end in intervals[1:]:
            if merged_intervals[-1][1] < start:
                merged_intervals.append([start,end])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1],end)
        return merged_intervals