# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        # Helper function to compute depth of a node and update diameter
        def depth(node):
            if not node:
                return 0
            # Compute depth of left and right children
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter: the longest path through this node
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the height of this node
            return 1 + max(left_depth, right_depth)
        
        # Compute depth starting from root, which updates diameter
        depth(root)
        
        # Return the maximum diameter found
        return self.diameter