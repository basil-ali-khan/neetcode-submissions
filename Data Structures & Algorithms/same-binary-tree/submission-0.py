# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are empty -> structurally identical at this point
        if not p and not q:
            return True
            
        # Base case 2: One node is empty, or the values don't match -> structural/value mismatch
        if not p or not q or p.val != q.val:
            return False
            
        # Recursive step: Both left and right subtrees must evaluate to True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)