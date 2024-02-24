# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = defaultdict(int)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                self.dic[root.val] += 1
                if root.right:
                    inorder(root.right) 
        inorder(root)
        r = sorted(self.dic.values())
        m = r.count(r[-1])
        l = sorted(self.dic.items() ,key=lambda x:x[1])
        ans = []
        for i in range(len(l) - 1,len(l) - m -1 ,-1):
            x, y = l[i]
            ans.append(x)
        return ans 