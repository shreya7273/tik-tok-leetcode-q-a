class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the area between the two pointers
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update the maximum area if current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area