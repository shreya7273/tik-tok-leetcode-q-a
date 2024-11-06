class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        left = 0  # Start of the sliding window
        max_length = 0  # Result for the maximum length of substring without repeats

        # Iterate through the string
        for right in range(len(s)):
            current_char = s[right]

            # If the character is already in the map and is within the window
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Move the start of the window to the right of the last occurrence of current_char
                left = char_index_map[current_char] + 1

            # Update the last seen index of the current character
            char_index_map[current_char] = right

            # Calculate the current length of substring without repeating characters
            current_length = right - left + 1
            # Update max_length if the current length is greater
            max_length = max(max_length, current_length)

        return max_length
        