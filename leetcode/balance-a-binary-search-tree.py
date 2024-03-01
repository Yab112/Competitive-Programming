# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root:
                inorder(root.left)
                self.res.append(root.val)
                inorder(root.right)
        def recursive(nodes):
            if not nodes:
                return
            mid = len(nodes)//2

            node = TreeNode(nodes[mid])
            node.left = recursive(nodes[:mid])
            node.right = recursive(nodes[mid + 1:])

            return node
        inorder(root)
        return recursive(self.res)

        