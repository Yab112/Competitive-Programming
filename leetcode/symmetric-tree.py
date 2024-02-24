class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inorder(root1,root2):
            if root1 and root2:
                return  root1.val == root2.val and inorder(root1.left,root2.right) and inorder(root1.right,root2.left)
            elif not root1 and not root2:
                return True
            return False
        return inorder(root,root)