class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        
        # Iterate through the array, fixing one number at a time
        for i in range(n):
            # Skip duplicate values to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find pairs that sum to -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Move the pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1  # Increase the sum by moving the left pointer to the right
                else:
                    right -= 1  # Decrease the sum by moving the right pointer to the left
        
        return triplets