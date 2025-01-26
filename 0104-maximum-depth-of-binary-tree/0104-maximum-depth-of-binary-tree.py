# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # BFS Implementation
        queue = deque([root])
        depth = 0
        
        while queue:
            level_size = len(queue) 
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)  # Enqueue left child
                if node.right:
                    queue.append(node.right)  # Enqueue right child
            
            # After processing the current level, increase depth
            depth += 1
        
        return depth