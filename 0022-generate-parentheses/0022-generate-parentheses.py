class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current, open_count, close_count):
            # If the current string has reached the maximum length, add it to the result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an open parenthesis if we still have some left to use
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a close parenthesis if it won't break the validity
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)
        return result
        