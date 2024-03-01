
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dic = {}
        
        def recursion(root, row, col):
            if root:
                if row not in self.dic:
                    self.dic[row] = [col]
                else:
                    self.dic[row].append(col)
                left = recursion(root.left, row + 1, 2 * col + 1)
                right = recursion(root.right, row + 1, 2 * col + 2)
                return left, right

        recursion(root, 0, 0)
        res = 0
        sorted_dic = sorted(self.dic.items())
        for target in sorted_dic:
            target = list(target)
            x ,y = target[1][0],target[1][-1]
            res = max(res ,y - x + 1)

        return res
