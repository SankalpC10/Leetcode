class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_freq = {}
        for curr_row in matrix:
            row_pattern = "".join(
                "T" if num ==curr_row[0] else "F" for num in curr_row
            )

            pattern_freq[row_pattern]  =(
                pattern_freq.get(row_pattern,0)+1
            )
        return max(pattern_freq.values(),default = 0)