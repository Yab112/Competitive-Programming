from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def forest(root, to_delete):
            if not root:
                return None

            root.left = forest(root.left, to_delete)
            root.right = forest(root.right, to_delete)

            if root.val in to_delete:
                if root.left:
                    self.arr.append(root.left)
                if root.right:
                    self.arr.append(root.right)
                return None
            return root

        if root.val not in to_delete:
            self.arr.append(root)

        forest(root, to_delete)
        
        return self.arr
