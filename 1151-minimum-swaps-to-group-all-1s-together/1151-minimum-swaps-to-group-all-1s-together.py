class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        
        max_ones = cur_ones = 0
        left = right = 0
        
        while right < len(data):
            cur_ones += data[right]
            
            right += 1
            
            if right- left > ones:
                cur_ones -= data[left]
                left += 1
                
            max_ones = max(max_ones, cur_ones)
            
        return ones - max_ones
                
                
        