# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def preorder(root):
            if root:
                if root.val >= low and root.val <= high:
                    self.arr.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return sum(self.arr)