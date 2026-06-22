class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        pattern_str = 'balloon'
        pattern_elem_freq = Counter(pattern_str)
        text_elem_freq = Counter(text)
        max_pattern_count = math.inf
        for char in pattern_str:
            max_pattern_count = min(max_pattern_count, text_elem_freq[char]// pattern_elem_freq[char])

        return max_pattern_count