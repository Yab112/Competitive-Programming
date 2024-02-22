# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        root = self._delete(root, key)
        return root

    def _delete(self, root, key):
        if not root:
            return root
        
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            successor = self._get_successor(root.right)
            root.val = successor.val
            root.right = self._delete(root.right, successor.val)
        
        return root

    def _get_successor(self, node):
        current = node
        while current.left:
            current = current.left
        return current
