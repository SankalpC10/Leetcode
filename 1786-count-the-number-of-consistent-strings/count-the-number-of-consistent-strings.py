class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Create a set to store the allowed characters
        allowed_chars = set(allowed)

        consistent_count = 0

        # Iterate through each word in the 'words' list
        for word in words:
            # Check if all characters in the word are in allowed_chars
            if all(char in allowed_chars for char in word):
                consistent_count += 1

        # Return the total count of consistent strings
        return consistent_count