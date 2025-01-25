# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        New_root = TreeNode(0)
        current = New_root
        def dfs(node):
            nonlocal current
            if node:
                dfs(node.left)
                current.right = TreeNode(node.val)
                current = current.right
                dfs(node.right)
        dfs(root)
        return New_root.right
        
        
                

            