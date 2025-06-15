class Solution:
    def generateTag(self, caption: str) -> str:
        res = "#"
        words = caption.split()
        first_word = True
        for word in words:
            filtered = ''.join(c.lower() for c in word if c.isalpha())
            if not filtered:
                continue
            if first_word:
                res+=filtered
                first_word =False
            else:
                res+=filtered.capitalize()
        return res[:100]