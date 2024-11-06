class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes (single character center)
            odd_palindrome = expand_around_center(i, i)
            # Check for even-length palindromes (two character center)
            even_palindrome = expand_around_center(i, i + 1)
            
            # Update the longest palindrome
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
        