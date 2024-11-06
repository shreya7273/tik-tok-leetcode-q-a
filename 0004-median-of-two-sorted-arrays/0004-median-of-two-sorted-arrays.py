class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # If there's nothing left on one side of the partition, use -infinity or infinity
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we have found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total length is odd
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If the total length is even
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            
            # Adjust the search range based on the comparison
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1
        