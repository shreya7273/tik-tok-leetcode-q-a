class Solution:
    def isPalindrome(self, x: int) -> bool:
           
        if x < 0:
            return False
        
       
        original_str = str(x)
        
        
        reversed_str = original_str[::-1]
        
        
        return original_str == reversed_str
