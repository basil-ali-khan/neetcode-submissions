# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base cases
        if not subRoot: 
            return True   # An empty tree is always a subtree of any tree
        if not root: 
            return False  # Main tree is empty, so it can't contain subRoot
            
        # 1. Check if they are identical starting from the current node
        if self.isSameTree(root, subRoot):
            return True
            
        # 2. Otherwise, check if subRoot is hidden somewhere in the left or right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Helper function from the 'Same Tree' problem
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)