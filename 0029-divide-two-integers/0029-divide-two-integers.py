class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # Prevent overflow

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize the quotient
        quotient = 0

        # Subtract divisor multiples from dividend using bit-shifting
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            # Subtract the current multiple from the dividend
            dividend -= temp_divisor
            quotient += multiple

        # Apply the sign to the quotient
        if negative:
            quotient = -quotient

        # Clamp the result within the 32-bit integer range
        return max(INT_MIN, min(INT_MAX, quotient))
        