class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        # Initialize the Roman numeral result
        roman = ""
        
        # Iterate through the symbols, reducing the number as you go
        for value, symbol in value_symbols:
            # Append the corresponding symbol while subtracting the value
            while num >= value:
                roman += symbol
                num -= value
        
        return roman
        