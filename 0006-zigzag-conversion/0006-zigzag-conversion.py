class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        # Create an array to hold the rows
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse through the string and fill the rows
        for char in s:
            rows[current_row] += char
            
            # If we are at the first or last row, we need to change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row
            current_row += 1 if going_down else -1
        
        # Join all rows and return the result
        return ''.join(rows)