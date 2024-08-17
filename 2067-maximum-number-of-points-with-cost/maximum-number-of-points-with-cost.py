class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prev_row = points[0]

        for row in range(1,rows):
            left_max = [0]*cols
            right_max = [0]*cols
            curr_row = [0]*cols

            left_max[0] = prev_row[0]
            for col in range(1,cols):
                left_max[col] = max(left_max[col - 1] - 1, prev_row[col])

            right_max[-1] = prev_row[-1]
            for col in range(cols-2, -1, -1):
                right_max[col] = max(right_max[col + 1] - 1, prev_row[col]) 

            for col in range(cols):
                curr_row[col] = points[row][col] + max(left_max[col], right_max[col])

            prev_row = curr_row
        return max(prev_row)

