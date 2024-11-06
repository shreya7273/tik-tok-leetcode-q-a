class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle the negative sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_x = 0
        while x != 0:
            digit = x % 10  # Get the last digit
            x //= 10  # Remove the last digit
            
            # Check for overflow/underflow before updating reversed_x
            if reversed_x > (INT_MAX // 10) or (reversed_x == INT_MAX // 10 and digit > 7):
                return 0  # Overflow condition
            reversed_x = reversed_x * 10 + digit
        
        # Apply the sign back
        reversed_x *= sign
        
        # Check for overflow in final result
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
        