# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total_sum = 0

        # Helper function for DFS traversal
        def dfs(node):
            if not node:
                return
            # If node's value is within range, add it to total_sum
            if low <= node.val <= high:
                self.total_sum += node.val
            # If node's value is greater than low, traverse the left subtree
            if node.val > low:
                dfs(node.left)
            # If node's value is less than high, traverse the right subtree
            if node.val < high:
                dfs(node.right)
        
        # Start DFS traversal from the root
        dfs(root)
        
        # Return the total sum
        return self.total_sum
        