# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = {}
        self.col =0
        self.row = 0
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def miniVertical(curHead,r,c):
            if curHead:
                if c not in self.dic:
                    self.dic[c] = []
                self.dic[c].append([r,c,curHead.val])
                if curHead.left:
                    miniVertical(curHead.left,r + 1,c - 1)
                if curHead.right:
                    miniVertical(curHead.right,r + 1,c + 1)
                
        miniVertical(root,self.row,self.row)
        for i in self.dic:
            self.dic[i].sort()
        list_dic = sorted(self.dic.items())
        res = []
        for i in list_dic:
            x,y = i
            temp = [j[-1] for j in y]
            res.append(temp)
        return res