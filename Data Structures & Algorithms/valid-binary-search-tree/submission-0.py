# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to track dynamic boundaries
        def validate(node, low, high):
            # Base case: an empty node is a valid BST
            if not node:
                return True
                
            # Current node value must strictly be within the boundaries
            if not (low < node.val < high):
                return False
                
            # Recursively check left and right subtrees with updated bounds
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
                    
        # Initialize with negative and positive infinity
        return validate(root, float('-inf'), float('inf'))