# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both nodes are greater, move to the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both nodes are smaller, move to the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # We found the split point! This node is the LCA.
            else:
                return curr