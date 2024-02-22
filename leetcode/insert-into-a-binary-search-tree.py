# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root 
        if cur == None:
            root = TreeNode(val)
        else:
            self._insert(val,cur)
        return root
    def _insert(self,value,cur_node):
        if value < cur_node.val:
            if cur_node.left == None:
                cur_node.left = TreeNode(value)
            else:
                self._insert(value,cur_node.left)
        elif value > cur_node.val:
            if cur_node.right ==None:
                cur_node.right = TreeNode(value)
            else:
                self._insert(value,cur_node.right)
    