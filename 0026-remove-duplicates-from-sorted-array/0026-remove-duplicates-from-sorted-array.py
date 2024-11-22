class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # Initialize the pointer for unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # Place the unique element at the correct position
                k += 1  # Move the pointer for the unique elements
        
        return k 