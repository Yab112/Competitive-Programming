# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int: 
        def recursion(root, min_val, max_val):
            if root is None:
                return 0
            
            min_el = min(root.val, min_val)
            max_el = max(root.val, max_val)
            
            left_diff = recursion(root.left, min_el, max_el)
            right_diff = recursion(root.right, min_el, max_el)
            
            return max(max_el - min_el, left_diff, right_diff)
        return recursion(root, root.val, root.val)
