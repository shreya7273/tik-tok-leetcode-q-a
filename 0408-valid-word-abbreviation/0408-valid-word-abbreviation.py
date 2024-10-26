class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # Pointers for word and abbr
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():  # If the current character in abbr is a letter
                if word[i] != abbr[j]:  # Letters must match
                    return False
                i += 1
                j += 1
            else:
                # Start of a number in abbr
                if abbr[j] == '0':  # Leading zeros are invalid
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])  # Build the number
                    j += 1
                i += num  # Move 'i' pointer in word by 'num' characters
        
        # Both pointers should reach the end of their respective strings
        return i == len(word) and j == len(abbr)
        