class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters (like on a phone keypad)
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        # List to store the results
        combinations = []
        
        # Backtracking function
        def backtrack(index: int, path: str):
            # If the current combination is complete (equal to the length of digits), add it to the results
            if index == len(digits):
                combinations.append(path)
                return
            
            # Get the letters corresponding to the current digit
            possible_letters = digit_to_letters[digits[index]]
            for letter in possible_letters:
                # Append the current letter and move to the next digit
                backtrack(index + 1, path + letter)
        
        # Start the backtracking with index 0 and an empty path
        backtrack(0, "")
        return combinations