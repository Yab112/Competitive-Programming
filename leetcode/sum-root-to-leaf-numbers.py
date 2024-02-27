# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
        self.cur = ""
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumRoot(curHead,curr):
            if curHead:
                curr += str(curHead.val)
                if not curHead.left  and not curHead.right:
                    self.arr.append(curr)
                if curHead.right:
                    sumRoot(curHead.right,curr)
                if curHead.left:
                    sumRoot(curHead.left,curr)
        sumRoot(root,self.cur)
        res = sum([int(i) for i in self.arr])
        return res

